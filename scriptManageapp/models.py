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
    name=models.CharField(u'姓名',max_length=30)
    email=models.CharField(u'邮箱',max_length=30)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    '''
    这项对应项目信息
    '''
    name=models.CharField(u'项目名称',max_length=30)
    proDesc=models.TextField(u'项目描述')
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

#下面为测试执行的结果

class Bug(models.Model):
    '''
    所有的Bug列表
    '''
    #执行的测试脚本
    script=models.ForeignKey(TestScript)
    screenShot=models.ManyToManyField(TestImage)
    bugDesc=models.TextField()

    def desc(self):
        return u'测试脚本%s出现了错误，错误描述为%s'%(
            self.script,self.screenShot
        )
#一次执行情况
class TestResaults(models.Model):
    '''
    代表一次执行的情况
    '''
    runDate=models.DateField()
    runTime=models.TimeField()
    runScripts=models.ManyToManyField(TestScript)
    bugs=models.ManyToManyField(Bug)
    failCount=models.IntegerField()
    successCount=models.IntegerField()

    def __str__(self):
        return u'%s'%(self.id)

    def desc(self):
        total=self.failCount+self.successCount
        return u'执行时间为%s-%s的测试执行了%d个测试脚本，有%d个执行失败'%(
            self.runDate,self.runTime,total,self.failCount
        )

    def report(self):
        '''
        用来生成报告的url
        :return:
        '''
        reportUrl='''<a href="www.baidu.com">报告链接</a>'''
        return reportUrl

class ResaultAdmin(admin.ModelAdmin):
    list_display = ["__str__","desc","report"]
    def save_model(self, request, obj, form, change):
        obj.user=request.user
        obj.save()
admin.site.register(TestResaults,ResaultAdmin)


class BugAdmin(admin.ModelAdmin):
    list_display = ['id','desc']
    def save_model(self, request, obj, form, change):
        obj.user=request.user
        obj.save()
admin.site.register(Bug,BugAdmin)