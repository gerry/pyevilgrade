from modules import ModuleBase


class NokiaSoftwareUpdate(ModuleBase):
    name = 'Nokia Software Update'
    version = '1.0'
    appver = '< 2.4.8'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = ''
    vh = '(nds2.fire.nokia.com)' 
    agent_filename = './agent/nokiafirmware.c0r'
    requests = [
        {   'path': '/oti/generic_files/Products',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': '',
        },
    ]