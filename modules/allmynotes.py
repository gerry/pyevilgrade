from modules import ModuleBase


class AllMyNotes(ModuleBase):
    name = 'Allmynotes'
    version = '1.0'
    appver = '< 1.26'
    author = ['German Rodriguez < grodriguez +[AT]+ infobytesec.com >']
    description = ''
    vh = '(www.vladonai.com)'
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
    requests = [{   
            'path': '/online_update_checker.php',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/allmynotes/version',
        }, {   
            'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }]
