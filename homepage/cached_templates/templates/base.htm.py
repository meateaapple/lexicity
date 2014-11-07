# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1415321520.928259
_enable_loop = True
_template_filename = '/Users/bradgessell/Documents/lexicity/homepage/templates/base.htm'
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
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js">    </script>\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body>\n  \n  <header class="top" role="header">\n    <div class="container">\n      <a href="#" class="navbar-brand pull-left">Lexicity</a>\n        <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n          <span class="glyphicon glyphicon-align-justify"></span>\n        </button>\n        <nav class="navbar-collapse collapse" role="navigation">\n          <ul class="navbar-nav nav">\n            <li><a href="/">Home</a></li>\n            <li><a href="/about/">About</a></li>\n            <li><a href="/video/">Videos</a></li>\n            <li><a href="/contact/">Contact</a></li>\n          </ul>\n        </nav>\n      </div>\n  </header>\n  \n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n    \n    \n  <div class="container large-ad">\n    <div class="row">\n      <div class="col-md-12" style="text-align: center;">\n        <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>\n        <!-- Banner Test -->\n        <ins class="adsbygoogle"\n             style="display:inline-block;width:728px;height:90px"\n             data-ad-client="ca-pub-4108381177414580"\n             data-ad-slot="7367531832"></ins>\n           <script>\n        (adsbygoogle = window.adsbygoogle || []).push({});\n        </script>\n      </div>\n    </div>\n  </div>\n  <div class="container mobile-ad">\n    <div class="row">\n      <div class="col-md-12" style="text-align: center;">\n          <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>\n        <!-- Language Home Ads -->\n          <ins class="adsbygoogle"\n             style="display:inline-block;width:320px;height:100px"\n             data-ad-client="ca-pub-4108381177414580"\n             data-ad-slot="5954517431"></ins>\n           <script>\n        (adsbygoogle = window.adsbygoogle || []).push({});\n        </script>\n      </div>\n    </div>\n  </div>\n  \n  <div class="bottom">\n    <div class="container">\n      <div class="row text-center">\n        <div class="col-md-4">\n        </div>\n        <div class="col-md-4">\n          <a href="https://www.facebook.com/lexicityonline" target="_blank">\n            <img src="static/homepage/media/New_facebook.png"/>\n          </a>\n          <a href="https://plus.google.com/+Lexicity" target="_blank">\n            <img src="static/homepage/media/New_googleplus.png"/>\n          </a>\n          <a href="https://www.twitter.com/lexicityonline" target="_blank">\n            <img src="static/homepage/media/New_twitter.png"/>\n          </a>\n          <h3>Send us resources <a href="contact">here</a>.</h3>\n        </div>\n        <div class="col-md-4">\n        </div>\n      </div>\n    </div>\n  </div>\n  \n')
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
{"uri": "base.htm", "source_encoding": "ascii", "filename": "/Users/bradgessell/Documents/lexicity/homepage/templates/base.htm", "line_map": {"33": 5, "34": 15, "35": 18, "36": 18, "37": 18, "42": 42, "43": 100, "44": 100, "45": 100, "16": 4, "18": 0, "51": 40, "57": 40, "27": 2, "28": 4, "29": 5, "63": 57}}
__M_END_METADATA
"""
