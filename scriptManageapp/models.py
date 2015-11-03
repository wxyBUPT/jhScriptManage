#coding=utf-8
from django.db import models
from django.contrib import admin
from django.template.loader import render_to_string
# Create your models here.



class ScriptAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","name"]

    def save_model(self, request, obj, form, change):
        obj.user=request.user
        obj.save()

class Developer(models.Model):
    '''
    开发者详细信息
    '''
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    '''
    这项对应项目信息
    '''
    name=models.CharField(max_length=30)
    proDesc=models.TextField()
    def __unicode__(self):
        return self.name

class Page(models.Model):
    '''
    对应项目中的某一个页面
    '''
    name=models.CharField(max_length=30)
    pageDesc=models.TextField()
    project=models.ForeignKey(Project)
    developers=models.ManyToManyField(Developer)

    def __unicode__(self):
        return self.name
class TestScript(models.Model):
    name=models.CharField(max_length=30)
    scriptPath=models.CharField(max_length=30)
    testPage=models.ManyToManyField(Page)

    def __unicode__(self):
        return self.name

class TestImage(models.Model):
    image=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=30)
    testScript=models.ForeignKey(TestScript)

    def thumbnail(self):
        image_path="""<img src="%s" height=40>"""%(self.image.url)
        return image_path

    def __unicode__(self):
        return self.name

class ImageAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","name","thumbnail"]

    def save_model(self, request, obj, form, change):
        obj.user=request.user
        obj.save()

admin.site.register(TestScript,ScriptAdmin)
admin.site.register(Project,ScriptAdmin)
admin.site.register(Page,ScriptAdmin)
admin.site.register(Developer,ScriptAdmin)
admin.site.register(TestImage,ImageAdmin)
