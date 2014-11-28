from django.contrib import admin
from homepage import models as hmod

admin.site.register(hmod.Language)
admin.site.register(hmod.Resource)
admin.site.register(hmod.Category)
admin.site.register(hmod.Recommendations)