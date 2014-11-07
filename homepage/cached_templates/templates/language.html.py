# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1415321569.705294
_enable_loop = True
_template_filename = '/Users/bradgessell/Documents/lexicity/homepage/templates/language.html'
_template_uri = 'language.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n  <div class="banner">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-12">\n          <h1>Akkadian</h1>\n        </div>\n      </div>\n      <div class="row">\n        <div class="col-md-12 subtitles">\n          <h2>The Akkadian language is the oldest attested Semitic language. It used the cuneiform style of writing and took its cuneiform in large part from Sumerian, an unrelated language.</h2>\n        </div>\n      </div>\n    </div>\n  </div>\n  <div class="middle">\n    <div class="container">\n      <div class="row">\n        <a href="dictionaries/">\n          <div class="col-md-4 tile">\n            <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/dict.png"/>\n            <h3>Dictionaries</h3>\n          </div>\n        </a>\n        <a href="grammars/">\n          <div class="col-md-4 tile">\n            <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/gram.png"/>\n            <h3>Grammars</h3>\n          </div>\n        </a>\n\t\t\t  <a href="charts/">\n\t\t\t    <div class="col-md-4 tile">\n            <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/chart.png"/>\n            <h3>Charts &amp; Aids</h3>\n          </div>\n\t\t\t   </a>\n\t\t   </div>\n       <div class="row">\n         <div class="col-md-2">\n         </div>\n         <a href="texts/">\n\t         <div class="col-md-4 tile">\n             <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/text.png"/>\n             <h3>Texts</h3>\n           </div>\n         </a>\n         <a href="other-resources/">\n           <div class="col-md-4 tile">\n             <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/other.png"/>\n             <h3>Other Resources</h3>\n           </div>\n         </a>\n         <div class="col-md-2">\n         </div>\n       </div>\n       <div class="row">\n         <div class="col-md-12" style="text-align: center;">\n           <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>\n           <!-- Banner Test -->\n           <ins class="adsbygoogle"\n                style="display:inline-block;width:728px;height:90px"\n                data-ad-client="ca-pub-4108381177414580"\n                data-ad-slot="7367531832"></ins>\n           <script>\n           (adsbygoogle = window.adsbygoogle || []).push({});\n           </script>\n         </div>\n       </div>\n     </div>\n   </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"35": 1, "68": 62, "45": 3, "27": 0, "52": 3, "53": 24, "54": 24, "55": 30, "56": 30, "57": 36, "58": 36, "59": 46, "60": 46, "61": 52, "62": 52}, "filename": "/Users/bradgessell/Documents/lexicity/homepage/templates/language.html", "uri": "language.html"}
__M_END_METADATA
"""
