# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414886483.330855
_enable_loop = True
_template_filename = '/Users/bradgessell/Documents/lexicity/homepage/templates/about.html'
_template_uri = 'about.html'
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
        __M_writer('\n  <div class="banner">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-12">\n          <h1>About</h1>\n        </div>\n      </div>\n      <div class="row">\n        <div class="col-md-12 subtitles">\n          <h2>If you\'ve ever felt alive studying something dead, you already know what it\'s about.</h2>\n        </div>\n      </div>\n    </div>\n  </div>\n  <div class="middle">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-2">\n        </div>\n        <div class="col-md-8">\n          <div class="info-text">\n            <p>Two years ago we launched Lexicity - a site dedicated to providing online study resources for ancient languages. We\'re happy to announce the second version of our site, which looks cleaner, runs more efficiently, and gets you to the resources faster.</p>\n\t          <p>With the second version, we\'re also committed to continual updates and expansion for language resources. We hope to include other languages soon as well, and we remain focused on creating an online community for learners of ancient languages.</p>\n\t\t\t      <p>So join in! Drop us a line over on our <a href="contact">contact page</a>. Pointers to new resources are always appreciated, or just share the love for languages. We\'re on <a href="https://www.twitter.com/lexicityonline" target="_blank">Twitter</a>, <a href="https://www.facebook.com/lexicityonline" target="_blank">Facebook</a>, and <a href="https://plus.google.com/+Lexicity" target="_blank">Google +</a>. Don\'t be shy - let\'s start learning together!</p>\n          </div>\n        </div>\n        <div class="col-md-2">\n        </div>\n      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "filename": "/Users/bradgessell/Documents/lexicity/homepage/templates/about.html", "uri": "about.html"}
__M_END_METADATA
"""
