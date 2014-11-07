from . import templater
from django_mako_plus.controller.router import view_function
from homepage import models as hmod

@view_function
def process_request(request):
  '''Main process function'''
  
  params = {
    "languages" : hmod.Language.objects.order_by("name").all(),
  }
  
  return templater.render_to_response(request, "index.html", params)