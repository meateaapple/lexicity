from . import templater
from django_mako_plus.controller.router import view_function
from homepage import models as hmod

@view_function
def process_request(request):
  '''Main process function'''
  
  language = hmod.Language.objects.get(name=request.urlparams[0])
  category = hmod.Category.objects.get(name=request.urlparams[1])
  resources = hmod.Resource.objects.filter(language=language, category=category)
  
  params = {
    "language" : language,
    "category" : category,
    "resources" : resources,
  }
  
  return templater.render_to_response(request, "resources.html", params)