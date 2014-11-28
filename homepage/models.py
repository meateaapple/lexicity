from django.db import models

class Language(models.Model):
  name = models.TextField(null=True, blank=True, unique=True)
  img_name = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)  
  
  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.TextField(null=True, blank=True, unique=True)
  img_name = models.TextField(null=True, blank=True)
  
  def __str__(self):
    return self.name

class Resource(models.Model):
  language = models.ForeignKey(Language)
  category = models.ForeignKey(Category)
  title = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  url = models.TextField(null=True, blank=True)
  
  def __str__(self):
    return "%s-%s: %s" % (self.language.name, self.category.name, self.title)
    
class Recommendations(models.Model):
  language = models.ForeignKey(Language)
  category = models.ForeignKey(Category)
  code = models.TextField(null=True, blank=True)
  
  def __str__(self):
    return "%s-%s" % (self.language.name, self.category.name)
  
