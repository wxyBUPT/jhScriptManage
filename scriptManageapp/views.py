#coding=utf-8
import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context,Template
from django.http import HttpResponse

from yunZhaoBiao.getUserHTML import getUserHTML

# Create your views here.
def runTest(request):
    htmlList=getUserHTML()
    con=Context({'htmllsit':htmlList})
    with open('/Users/cy-openstack/PycharmProjects/jhScriptManage'
              '/scriptManageapp/template/emailTemplate.html') as f:
        text=f.read()
        print u'读出的数据'
        print text
        t=Template(text)
    html=t.render(con)
    print u'调用了这个函数'
    print html
    return HttpResponse(html)