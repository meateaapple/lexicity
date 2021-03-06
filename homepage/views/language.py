from . import templater
from django_mako_plus.controller.router import view_function
from homepage import models as hmod

@view_function
def process_request(request):
  '''Main process function'''
  
  params = {
    "language" : hmod.Language.objects.get(name=request.urlparams[0]),
    "categories" : hmod.Category.objects.all(),
  }
  
  return templater.render_to_response(request, "language.html", params)