# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414295667.208334
_enable_loop = True
_template_filename = '/Users/bradgessell/Documents/lexicity/homepage/templates/contact.html'
_template_uri = 'contact.html'
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
        __M_writer('\n  <div class="banner">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-12">\n          <h1>Contact</h1>\n        </div>\n      </div>\n    </div>\n  </div>\n  <div class="middle">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-8">\n          <form action="contact.php" method="post">\n            <h3>Your name: <input type="text" name="cf_name"></h3>\n            <h3>Your email: <input type="text" name="cf_email"></h3>\n            <h3>Message: <textarea name="cf_message" rows="10" cols="20">Type your message here.</textarea></h3>\n            <input type="submit" value="Send">\n            <input type="reset" value="Clear">\n          </form>\n        </div>\n        <div class="col-md-4">\n    \t\t\t<a class="twitter-timeline" href="https://twitter.com/lexicityonline" data-widget-id="365946994956566528">Tweets by @lexicityonline</a>\n      \t\t<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?\'http\':\'https\';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>\n        </div>\n      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "contact.html", "source_encoding": "ascii", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "filename": "/Users/bradgessell/Documents/lexicity/homepage/templates/contact.html"}
__M_END_METADATA
"""