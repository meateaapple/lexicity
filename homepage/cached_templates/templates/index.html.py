# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414295112.36424
_enable_loop = True
_template_filename = '/Users/bradgessell/Documents/lexicity/homepage/templates/index.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        languages = context.get('languages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <div class="content">\n    <div class="banner">\n      <div class="container">\n        <div class="row">\n          <div class="col-md-12">\n            <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/lexicity_logo.png" alt="Lexicity logo"/>\n          </div>\n        </div>\n        <div class="row">\n          <div class="col-md-12 subtitles">\n            <h2>The first and only comprehensive index for ancient language resources on the internet.</h2>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n  <div class="middle">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-12 content">\n          <h2>Choose Your Language</h2>\n        </div>\n      </div>\n      <div class="row">\n        \n')
        for language in languages:
            __M_writer('      \n        <a href="')
            __M_writer(str( language ))
            __M_writer('">\n          <div class="col-md-3 tile">\n            <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/')
            __M_writer(str( language ))
            __M_writer('.png"/>\n            <h3>')
            __M_writer(str( language ))
            __M_writer('</h3>\n          </div>\n        </a>\n        \n')
        __M_writer('      \n      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "source_encoding": "ascii", "line_map": {"64": 33, "65": 34, "66": 34, "27": 0, "36": 1, "73": 67, "46": 3, "67": 39, "54": 3, "55": 9, "56": 9, "57": 29, "58": 30, "59": 31, "60": 31, "61": 33, "62": 33, "63": 33}, "filename": "/Users/bradgessell/Documents/lexicity/homepage/templates/index.html"}
__M_END_METADATA
"""
