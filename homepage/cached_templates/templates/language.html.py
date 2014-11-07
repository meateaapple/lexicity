# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1415382887.520863
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
        def content():
            return render_content(context._locals(__M_locals))
        language = context.get('language', UNDEFINED)
        categories = context.get('categories', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        language = context.get('language', UNDEFINED)
        categories = context.get('categories', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <div class="banner">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-12">\n          <h1>')
        __M_writer(str( language.name ))
        __M_writer('</h1>\n        </div>\n      </div>\n      <div class="row">\n        <div class="col-md-12 subtitles">\n          <h2>')
        __M_writer(str( language.description ))
        __M_writer('</h2>\n        </div>\n      </div>\n    </div>\n  </div>\n  <div class="middle">\n    <div class="tile_container text-center">\n      \n')
        for category in categories:
            __M_writer('\n          <a href="/resources/')
            __M_writer(filters.url_escape(str( language.name)))
            __M_writer('/')
            __M_writer(filters.url_escape(str( category.name)))
            __M_writer('/">\n            <div class="tile resource-tile">\n              <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/')
            __M_writer(str( category.img_name ))
            __M_writer('"/>\n              <h3>')
            __M_writer(str( category.name ))
            __M_writer('</h3>\n            </div>\n          </a>\n        \n')
        __M_writer('        \n     </div>\n   </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 24, "65": 24, "66": 24, "67": 26, "68": 26, "69": 26, "70": 26, "71": 27, "72": 27, "73": 32, "79": 73, "27": 0, "37": 1, "47": 3, "56": 3, "57": 9, "58": 9, "59": 14, "60": 14, "61": 22, "62": 23, "63": 24}, "source_encoding": "ascii", "uri": "language.html", "filename": "/Users/bradgessell/Documents/lexicity/homepage/templates/language.html"}
__M_END_METADATA
"""
