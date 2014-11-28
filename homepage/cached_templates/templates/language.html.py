# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1417099314.422328
_enable_loop = True
_template_filename = '/Users/bradgessell/Documents/lexicity/lexicity/homepage/templates/language.html'
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
        language = context.get('language', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        enumerate = context.get('enumerate', UNDEFINED)
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
        language = context.get('language', UNDEFINED)
        def content():
            return render_content(context)
        enumerate = context.get('enumerate', UNDEFINED)
        categories = context.get('categories', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <div class="banner">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-12">\n          <h1>')
        __M_writer(str( language.name ))
        __M_writer('</h1>\n        </div>\n      </div>\n      <div class="row">\n        <div class="col-md-12 subtitles">\n          <h2>')
        __M_writer(str( language.description ))
        __M_writer('</h2>\n        </div>\n      </div>\n    </div>\n  </div>\n  <div class="middle">\n    <div class="container text-center">\n      <div class="row">\n      \n')
        for i, category in enumerate(categories):
            __M_writer('\n          <a href="/resources/')
            __M_writer(filters.url_escape(str( language.name)))
            __M_writer('/')
            __M_writer(filters.url_escape(str( category.name)))
            __M_writer('/">\n            <div class="col-md-4 tile">\n              <!--<img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/"/>-->\n              <span class="glyphicon ')
            __M_writer(str( category.img_name ))
            __M_writer(' category-image"></span>\n              <h3 class="tile-title">')
            __M_writer(str( category.name ))
            __M_writer('</h3>\n            </div>\n          </a>\n        \n')
            if i == 2:
                __M_writer('        \n        </div>\n        <div class="row">\n          <div class="col-md-2">\n          </div>\n         \n')
            __M_writer('        \n')
        __M_writer('        <div class="col-md-2">\n        </div>\n      </div>\n      <div class="row text-center">\n        <div class="col-md-12">\n          <a href="/">\n            <button type="button" class="btn btn-default btn-lg"><span class="glyphicon glyphicon-arrow-left"></span> Back to Languages</button>\n          </a>\n        </div>\n      </div>\n     </div>\n   </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/bradgessell/Documents/lexicity/lexicity/homepage/templates/language.html", "line_map": {"64": 24, "65": 25, "66": 25, "67": 25, "68": 25, "69": 27, "70": 27, "71": 28, "72": 28, "73": 29, "74": 29, "75": 33, "76": 34, "77": 41, "78": 43, "84": 78, "27": 0, "38": 1, "48": 3, "58": 3, "59": 9, "60": 9, "61": 14, "62": 14, "63": 23}, "uri": "language.html"}
__M_END_METADATA
"""
