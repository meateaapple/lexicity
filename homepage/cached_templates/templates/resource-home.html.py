# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414546651.619955
_enable_loop = True
_template_filename = '/Users/bradgessell/Documents/lexicity/homepage/templates/resource-home.html'
_template_uri = 'resource-home.html'
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
        __M_writer = context.writer()
        __M_writer('\n\n  <div class="banner">\n    <div class="container">\n      <div class"row">\n        <div class="col-md-12">\n        </div>\n      </div>\n      <div class="row">\n        <div class="col-md-12">\n          <h1>Akkadian Charts &amp; Aids</h1>\n        </div>\n      </div>\n      <div class="row">\n        <div class="col-md-12 subtitles">\n          <h2>Akkadian is related to Hebrew and Arabic.</h2>\n        </div>\n      </div>\n    </div>\n  </div>\n  \n  <div class="middle">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-2">\n        </div>\n        <div class="col-md-8">\n          <table class="resource-table">\n            <tr>\n              <th>Resource</th>\n              <th>Description</th>\n            </tr>\n            <tr>\n              <td>\n                <a href="http://www.sron.nl/~jheise/akkadian/Welcome_list.html">Cuneiform Sign-Lists Online</a>\n              </td>\n              <td>A few different lists.</td>\n            </tr>\n            <tr>\n              <td>\n                <a href="http://www.sron.nl/~jheise/akkadian/title.html">Translating Cuneiform</a>\n              </td>\n              <td>A helpful set of steps with links to different books and print resources.</td>\n            </tr>\n            <tr>\n              <td>\n                <a href="http://www.lexicity.com/downloads/akkadian_grammar_wiki.pdf">Akkadian Grammar</a>\n              </td>\n              <td>A PDF file.</td>\n            </tr>\n            <tr>\n              <td colspan="2">\n                <a href="../">\n                  <button type="button" class="btn btn-default btn-lg"><span class="glyphicon glyphicon-arrow-left"></span> Back to Akkadian Resources</button>\n                </a>\n              </td>\n            </tr>\n          </table>\n        </div>\n        <div class="col-md-2">\n        </div>\n      </div>\n      <div class="row">\n        <div class="col-md-12" style="text-align: center;">\n          <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>\n          <!-- Banner Test -->\n          <ins class="adsbygoogle"\n               style="display:inline-block;width:728px;height:90px"\n               data-ad-client="ca-pub-4108381177414580"\n               data-ad-slot="7367531832"></ins>\n          <script>\n          (adsbygoogle = window.adsbygoogle || []).push({});\n          </script>\n        </div>\n      </div>\n    </div>\n  </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "uri": "resource-home.html", "source_encoding": "ascii", "filename": "/Users/bradgessell/Documents/lexicity/homepage/templates/resource-home.html"}
__M_END_METADATA
"""
