from modules import ModuleBase


class openbazaar(ModuleBase):
    name = 'openbazaar'
    version = '1.0'
    appver = 'All'
    author = ['Matias Ariel Re Medina <mre[at]infobytesec[dot]com>']
    description = """OpenBazaar update.'""",
    vh = '(updates.openbazaar.org)' 
    requests = [
        {   'path': 'update\/\w+\/',
            'type': 'string',
            'method': '',
            'bin': '0',
            'string': '{"url": "http://updates.openbazaar.org/download/v<%VERSION%>/<%FILENAME%>","name": "<%VERSION%>","notes": "Lastest update available.\r\n\r\n\r\n## Hashes\r\n\r\n**<%FILENAME%>**\r\n<%AGENTSHA256%>\n","pub_date": "<%PUBDATE%>"}',
            'parse': '1',
            'file': '',
        },
        {   'path': '.exe|.dmg',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '0',
            'file': ''
        }
    ]
    options = {
        'filename': {
            'val' : "OpenBazaar-1.1.6_Setup_i386.exe",
            'desc': 'Client name.'
        },
        'version': {
            'val': '1.1.6',
            'desc': 'Version name of the client.'
        },
        'pubdate': {
            'val': '2016-06-07T02:13:05.000Z',
            'desc': 'Publication date of current update.'
        },
    }