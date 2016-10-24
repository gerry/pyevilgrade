from modules import ModuleBase


class PandaAntirootkit(ModuleBase):
    name = 'Panda Antirootkit'
    version = '1.0'
    appver = ''
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = ''
    vh = '(acs.pandasoftware.com|suspects.pandasoftware.com)'
    requests = [{
            'path': '/upglitenv/tucan/Upgrade.phtml',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': 'lastversion=5.0.0.20\nurl=http://acs.pandasoftware.com/upglite/tucan/PAVARK.exe\nlicense=5.0.0.0',
            'parse': 0,
            'file': '',
        }, {
            'path': '/rootkits/sendfile.aspx',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': 'foo',
            'parse': 0,
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