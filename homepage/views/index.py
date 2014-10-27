from . import templater
from django_mako_plus.controller.router import view_function

@view_function
def process_request(request):
  '''Main process function'''
  
  languages = ["Akkadian", "Arabic", "Aramaic",]
  params = {"languages" : languages}
  
  return templater.render_to_response(request, "index.html", params)