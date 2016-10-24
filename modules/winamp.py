from modules import ModuleBase


class Winamp(ModuleBase):
    name = 'Winamp'
    version = '1.0'
    appver = '< 5.581'
    author = ['Francisco Amato < famato +[AT]+ infobyte.com>']
    description = ''
    vh = '(www.winamp.com|client.winamp.com)'
    requests = [{
            'path': '/update/latest-version.php',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string' : "",
            'parse': 1,
            'file': './include/winamp/latest-version.php',
        }, {
           'path': '/update/client/notice.php',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 0,
            'file': './include/winamp/notice.php',
        }, {
            'path': '(/update/client_session.php|/nowplaying/mini|/update/do_im.php)',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 0,
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
