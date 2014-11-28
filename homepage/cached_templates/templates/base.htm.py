# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1417099311.91625
_enable_loop = True
_template_filename = '/Users/bradgessell/Documents/lexicity/lexicity/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    \n    <title>Lexicity</title>\n    \n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js">    </script>\n    <script>\n      (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\n      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n      })(window,document,\'script\',\'//www.google-analytics.com/analytics.js\',\'ga\');\n\n      ga(\'create\', \'UA-30676234-1\', \'auto\');\n      ga(\'send\', \'pageview\');\n\n    </script>\n    \n    <script src="https://apis.google.com/js/platform.js" async defer></script>\n    \n    <!-- Go to www.addthis.com/dashboard to customize your tools -->\n    <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-5463c10e2ad6f4c1" async="async"></script>\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body>\n  \n  <header class="top" role="header">\n    <div class="container">\n      <a href="/" class="navbar-brand pull-left">Lexicity</a>\n      <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n        <span class="glyphicon glyphicon-align-justify"></span>\n      </button>\n      <nav class="navbar-collapse collapse" role="navigation">\n        <ul class="navbar-nav nav">\n          <li><a href="/">Home</a></li>\n          <li><a href="/about/">About</a></li>\n          <li><a href="http://lexicityonline.tumblr.com" target="_blank">Blog</a></li>\n          <li><a href="/contact/">Contact</a></li>\n        </ul>\n      </nav>\n    </div>\n  </header>\n  \n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n  \n  <div class="bottom">\n    <div class="container large-ad">\n      <div class="row">\n        <div class="col-md-12" style="text-align: center;">\n          <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>\n          <!-- Banner Test -->\n          <ins class="adsbygoogle"\n               style="display:inline-block;width:728px;height:90px"\n               data-ad-client="ca-pub-4108381177414580"\n               data-ad-slot="7367531832"></ins>\n             <script>\n          (adsbygoogle = window.adsbygoogle || []).push({});\n          </script>\n        </div>\n      </div>\n    </div>\n    <div class="container mobile-ad">\n      <div class="row">\n        <div class="col-md-12" style="text-align: center;">\n            <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>\n          <!-- Language Home Ads -->\n            <ins class="adsbygoogle"\n               style="display:inline-block;width:320px;height:100px"\n               data-ad-client="ca-pub-4108381177414580"\n               data-ad-slot="5954517431"></ins>\n             <script>\n          (adsbygoogle = window.adsbygoogle || []).push({});\n          </script>\n        </div>\n      </div>\n    </div>\n    <div class="container">\n      <div class="row text-center">\n        <div class="col-md-12">\n          <a href="http://www.facebook.com/lexicityonline" target="_blank" class="social_button">\n            <img src="/static/homepage/media/facebook.png"/>\n          </a>\n          <a href="http://plus.google.com/+Lexicity" rel="publisher" target="_blank" class="social_button">\n            <img src="/static/homepage/media/googleplus.png"/>\n          </a>\n          <a href="http://www.twitter.com/lexicityonline" target="_blank" class="social_button">\n            <img src="/static/homepage/media/twitter.png"/>\n          </a>\n          <a href="http://lexicityonline.tumblr.com" target="_blank" class="social_button">\n            <img src="/static/homepage/media/tumblr.png"/>\n          </a>\n          <a href="http://www.youtube.com/channel/UCUvkgZNXd7nv5w-j9X7G7DQ/videos" target="_blank" class="social_button">\n            <img src="/static/homepage/media/youtube.png"/>\n          </a>\n        </div>\n      </div>\n      <div class="row text-center">\n        <div class="col-md-12">\n          <button type="button" class="btn btn-warning btn-lg top-buffer" data-toggle="modal" data-target="#signup">\n            Subscribe To Our Mailing List\n          </button>\n          <div class="modal fade" id="signup">\n            <div class="modal-dialog">\n              <div class="modal-content">\n                <div class="modal-header">\n                  <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>\n                  <h4 class="modal-title">Subscribe To Our Mailing List</h4>\n                </div>\n                <div class="modal-body text-center">\n                  \n                 <!-- Begin MailChimp Signup Form -->\n                 <link href="//cdn-images.mailchimp.com/embedcode/slim-081711.css" rel="stylesheet" type="text/css">\n                 <style type="text/css">\n                 \t#mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; }\n                 \t/* Add your own MailChimp form style overrides in your site stylesheet or in this style block.\n                 \t   We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */\n                 </style>\n                 <div id="mc_embed_signup">\n                 <form action="//lexicity.us9.list-manage.com/subscribe/post?u=daade0457d3e1b477f11374da&amp;id=5d62e3f5a7" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>\n                     <div id="mc_embed_signup_scroll">\n                 \t<input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>\n                     <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->\n                     <div style="position: absolute; left: -5000px;"><input type="text" name="b_daade0457d3e1b477f11374da_5d62e3f5a7" tabindex="-1" value=""></div>\n                     <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>\n                     </div>\n                 </form>\n                 </div>\n\n                 <!--End mc_embed_signup-->\n                  \n                  \n                </div>\n                <div class="modal-footer">\n                  <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n                </div>\n              </div><!-- /.modal-content -->\n            </div><!-- /.modal-dialog -->\n          </div><!-- /.modal -->\n          <p>&copy; 2014 Lexicity</p>\n        </div>\n      </div>\n    </div>\n  </div>\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n      Site content goes here in sub-templates.\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/bradgessell/Documents/lexicity/lexicity/homepage/templates/base.htm", "line_map": {"33": 5, "34": 15, "35": 33, "36": 33, "37": 33, "42": 57, "43": 159, "44": 159, "45": 159, "16": 4, "18": 0, "51": 55, "57": 55, "27": 2, "28": 4, "29": 5, "63": 57}, "uri": "base.htm"}
__M_END_METADATA
"""
