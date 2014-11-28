# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1417099316.026154
_enable_loop = True
_template_filename = '/Users/bradgessell/Documents/lexicity/lexicity/homepage/templates/resources.html'
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
        category = context.get('category', UNDEFINED)
        language = context.get('language', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        recommendations = context.get('recommendations', UNDEFINED)
        resources = context.get('resources', UNDEFINED)
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
        category = context.get('category', UNDEFINED)
        language = context.get('language', UNDEFINED)
        def content():
            return render_content(context)
        recommendations = context.get('recommendations', UNDEFINED)
        resources = context.get('resources', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <div class="banner">\n    <div class="container">\n      <div class"row">\n        <div class="col-md-12">\n        </div>\n      </div>\n      <div class="row">\n        <div class="col-md-12">\n          <h1>')
        __M_writer(filters.html_escape(str( language.name )))
        __M_writer(' ')
        __M_writer(filters.html_escape(str( category.name )))
        __M_writer('</h1>\n        </div>\n      </div>\n      <div class="row">\n        <div class="col-md-12 text-center">\n          <button type="button" class="btn btn-warning btn-lg top-buffer" data-toggle="modal" data-target="#myModal">\n            See Recommendations\n          </button>\n          <div class="modal fade" id="myModal">\n            <div class="modal-dialog">\n              <div class="modal-content">\n                <div class="modal-header">\n                  <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>\n                  <h4 class="modal-title">Lexicity Recommendations</h4>\n                </div>\n                <div class="modal-body">\n                  \n')
        if recommendations.count() == 0:
            __M_writer('                  \n                    <p>There are no recommendations for ')
            __M_writer(filters.html_escape(str( language.name )))
            __M_writer(' ')
            __M_writer(filters.html_escape(str( category.name )))
            __M_writer(' yet. <a href="/contact/">Contact us</a> and tell us what to recommend!</p>\n                    <p>Please accept our apologies. You can watch <a href="https://www.youtube.com/watch?v=CMNry4PE93Y" target="_blank">this video</a> instead.</p>\n                    \n')
        else: 
            __M_writer('                  \n')
            for r in recommendations:
                __M_writer('                      <div class="recommendations">\n                        \n                        ')
                __M_writer(str( r.code ))
                __M_writer('\n                        \n                      </div>\n')
            __M_writer('                  \n')
        __M_writer('                  \n                  \n                </div>\n                <div class="modal-footer">\n                  <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n                </div>\n              </div><!-- /.modal-content -->\n            </div><!-- /.modal-dialog -->\n          </div><!-- /.modal -->\n        </div>\n      </div>\n    </div>\n  </div>\n  \n  <div class="middle">\n    <div class="container">\n      <div class="row top-buffer text-center">\n        <div class="col-md-12">\n          <a href="/language/')
        __M_writer(str( language.name ))
        __M_writer('/">\n            <button type="button" class="btn btn-default btn-lg"><span class="glyphicon glyphicon-arrow-left"></span> Back to ')
        __M_writer(filters.html_escape(str( language.name )))
        __M_writer(' Resources</button>\n          </a>\n        </div>\n      </div>\n      <div class="row">\n        <div class="col-md-2">\n        </div>\n        <div class="col-md-8">\n          <table class="resource-table">\n            <tr>\n              <th width="45%">Resource</th>\n              <th width="45%">Description</th>\n              <th width="10%"/>\n            </tr>\n            \n')
        if resources.count() == 0:
            __M_writer('            \n              <tr>\n                <td colspan="3">\n                  <p>Darn it! We\'re still working on getting some ')
            __M_writer(str( language.name ))
            __M_writer(' ')
            __M_writer(str( category.name ))
            __M_writer(' up. Have some you want to see? <a href="/contact/">Contact us</a> and tell us what to recommend!</p>\n                  <p>In the meantime, <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank">this video</a> may be what you\'re looking for.</p>\n                </td>\n              </tr>\n              \n')
        else:
            __M_writer('            \n')
            for resource in resources:
                __M_writer('            \n            <tr>\n              <td>\n                <a href="')
                __M_writer(str( resource.url ))
                __M_writer('" target="_blank">')
                __M_writer(filters.html_escape(str( resource.title )))
                __M_writer('</a>\n              </td>\n              <td>')
                __M_writer(filters.html_escape(str( resource.description )))
                __M_writer('</td>\n              <td>\n                <a href="')
                __M_writer(str( resource.url ))
                __M_writer('" target="_blank">\n                  <button type="button" class="btn btn-default">Go <span class="glyphicon glyphicon-arrow-right"></span></button>\n                </a>\n              </td>\n            </tr> \n            \n')
            __M_writer('            \n')
        __M_writer('          \n            </tr>\n          </table>\n        </div>\n        <div class="col-md-2">\n        </div>\n      </div>\n      <div class="row text-center">\n        <div class="col-md-12">\n          <a href="/language/')
        __M_writer(str( language.name ))
        __M_writer('/">\n            <button type="button" class="btn btn-default btn-lg"><span class="glyphicon glyphicon-arrow-left"></span> Back to ')
        __M_writer(filters.html_escape(str( language.name )))
        __M_writer(' Resources</button>\n          </a>\n        </div>\n      </div>\n      \n        </div>\n      </div>\n    </div>\n  </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/bradgessell/Documents/lexicity/lexicity/homepage/templates/resources.html", "line_map": {"27": 0, "38": 1, "48": 3, "58": 3, "59": 13, "60": 13, "61": 13, "62": 13, "63": 30, "64": 31, "65": 32, "66": 32, "67": 32, "68": 32, "69": 35, "70": 36, "71": 37, "72": 38, "73": 40, "74": 40, "75": 44, "76": 46, "77": 64, "78": 64, "79": 65, "80": 65, "81": 80, "82": 81, "83": 84, "84": 84, "85": 84, "86": 84, "87": 89, "88": 90, "89": 91, "90": 92, "91": 95, "92": 95, "93": 95, "94": 95, "95": 97, "96": 97, "97": 99, "98": 99, "99": 106, "100": 108, "101": 117, "102": 117, "103": 118, "104": 118, "110": 104}, "uri": "resources.html"}
__M_END_METADATA
"""
