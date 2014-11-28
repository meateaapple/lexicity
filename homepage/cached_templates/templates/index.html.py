# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1417099311.904589
_enable_loop = True
_template_filename = '/Users/bradgessell/Documents/lexicity/lexicity/homepage/templates/index.html'
_template_uri = 'index.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        languages = context.get('languages', UNDEFINED)
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
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        languages = context.get('languages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <div class="content">\n    <div class="banner">\n      <div class="container">\n        <div class="row">\n          <div class="col-md-12">\n            <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/lexicity_logo.png" alt="Lexicity logo"/>\n          </div>\n        </div>\n        <div class="row">\n          <div class="col-md-12 subtitles">\n            <h2>The first and only comprehensive index for ancient language resources on the internet.</h2>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n  <div class="middle">\n    <div class="container text-center">\n      <div class="row">\n        <div class="col-md-12 content">\n          <h2>Choose Your Language</h2>\n        </div>\n      </div>\n      <div class="row">\n        \n')
        for i, language in enumerate(languages):
            __M_writer('      \n      <div class="col-md-3 tile">\n        <a href="/language/')
            __M_writer(filters.url_escape(str( language.name)))
            __M_writer('/">\n          <div>\n            <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/')
            __M_writer(str( language.img_name ))
            __M_writer('"/>\n            <h3>')
            __M_writer(str( language ))
            __M_writer('</h3>\n          </div>\n        </a>\n      </div>\n      \n')
            if i % 4 == 3 and i > 0:
                __M_writer('      \n        </div>\n        <div class="row">\n      \n')
            __M_writer('\n')
        __M_writer('      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/bradgessell/Documents/lexicity/lexicity/homepage/templates/index.html", "line_map": {"64": 34, "65": 34, "66": 34, "27": 0, "68": 35, "37": 1, "70": 41, "71": 46, "72": 48, "78": 72, "47": 3, "67": 35, "69": 40, "56": 3, "57": 9, "58": 9, "59": 29, "60": 30, "61": 32, "62": 32, "63": 34}, "uri": "index.html"}
__M_END_METADATA
"""
