from modules import ModuleBase


class Gom(ModuleBase):
    name = 'Gom'
    version = '1.0'
    appver = '< 2.1.25.5015'
    author = ['German Rodriguez < grodriguez +[AT]+ infobytesec.com >']
    description = ''
    vh = '(app.gomlab.com)' 
    requests = [
        {   'path': '/eng/gom/GrVersionEN.ini',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/gom/gom.ini',
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
