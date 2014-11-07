# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1415383461.946897
_enable_loop = True
_template_filename = '/Users/bradgessell/Documents/lexicity/homepage/templates/resources.html'
_template_uri = 'resources.html'
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
        resources = context.get('resources', UNDEFINED)
        category = context.get('category', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        language = context.get('language', UNDEFINED)
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
        resources = context.get('resources', UNDEFINED)
        category = context.get('category', UNDEFINED)
        def content():
            return render_content(context)
        language = context.get('language', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <div class="banner">\n    <div class="container">\n      <div class"row">\n        <div class="col-md-12">\n        </div>\n      </div>\n      <div class="row">\n        <div class="col-md-12">\n          <h1>')
        __M_writer(filters.html_escape(str( language.name )))
        __M_writer(' ')
        __M_writer(filters.html_escape(str( category.name )))
        __M_writer('</h1>\n        </div>\n      </div>\n    </div>\n  </div>\n  \n  <div class="middle">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-2">\n        </div>\n        <div class="col-md-8">\n          <table class="resource-table">\n            <tr>\n              <th>Resource</th>\n              <th>Description</th>\n            </tr>\n            \n')
        for resource in resources:
            __M_writer('            \n            <tr>\n              <td><a href="')
            __M_writer(str( resource.url ))
            __M_writer('" target="_blank">')
            __M_writer(filters.html_escape(str( resource.title )))
            __M_writer('</a></td>\n              <td>')
            __M_writer(filters.html_escape(str( resource.description )))
            __M_writer('</td>\n            </tr> \n            \n')
        __M_writer('          \n              <td colspan="2">\n                <a href="/language/')
        __M_writer(str( language.name ))
        __M_writer('/">\n                  <button type="button" class="btn btn-default btn-lg"><span class="glyphicon glyphicon-arrow-left"></span> Back to ')
        __M_writer(filters.html_escape(str( language.name )))
        __M_writer(' Resources</button>\n                </a>\n              </td>\n            </tr>\n          </table>\n        </div>\n        <div class="col-md-2">\n        </div>\n      </div>\n    </div>\n  </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 34, "65": 34, "66": 34, "67": 35, "68": 35, "69": 39, "70": 41, "71": 41, "72": 42, "73": 42, "79": 73, "27": 0, "37": 1, "47": 3, "56": 3, "57": 13, "58": 13, "59": 13, "60": 13, "61": 31, "62": 32, "63": 34}, "source_encoding": "ascii", "uri": "resources.html", "filename": "/Users/bradgessell/Documents/lexicity/homepage/templates/resources.html"}
__M_END_METADATA
"""
