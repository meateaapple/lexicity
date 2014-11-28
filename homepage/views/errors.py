from django.http import HttpResponseRedirect
from django_mako_plus.controller.router import view_function

def error404(request):

  return HttpResponseRedirect('/')