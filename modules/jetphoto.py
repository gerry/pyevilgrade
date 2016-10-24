from modules import ModuleBase


class JetPhoto(ModuleBase):
    name = 'JetPhoto'
    version = '1.0'
    appver = '< 4.7.2'
    author = ['German Rodriguez < grodriguez +[AT]+ infobytesec.com >']
    description = ''
    vh = '(www.jetphotosoft.com)' 
    requests = [
        {   'path': '/updater/\?software\=JPStudio\-Win\-V2',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/jetphoto/version',
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