from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# 导入应用app_manage模块下的Project表
from telephone_manage.models import tels

# 导入form表单，用来添加项目使用
from telephone_manage.forms import ProjectForm, ProjectEditForm

from django.http import HttpResponseRedirect

from django.db import models

from telephone_manage.models import tels

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# 装饰器，添加上后可判断登录状态。若登录则允许访问，不登录不允许访问这个路径 http://127.0.0.1:8000/manage/
@login_required
def manage(requests):
    Projects = tels.objects.all()
    p = Paginator(Projects,10)
    page = requests.GET.get("page", "")
    if page == " ":
        page = 1
    try:
        page_projects = p.page(page)
    except EmptyPage:
        page_projects = p.page(p.num_pages)
    except PageNotAnInteger:
        page_projects = p.page(1)
    return render(requests, "project_list.html", {"projects": page_projects})


def project_add(requests):
    if requests.method == "POST":
        form = ProjectForm(requests.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            #fund_q = models.tels.objects.filter(pk=1).first()
            #fund = form.cleaned_data['fund_q.get_sys_display()']
            fund = form.cleaned_data['fund']
            sys = form.cleaned_data['sys']
            type = form.cleaned_data['type']
            version = form.cleaned_data['version']
            tels.objects.create(name=name,fund=fund,sys=sys,type=type,version=version)
        return HttpResponseRedirect("/project/")
    else:
        form = ProjectForm()
    return render(requests,'project_add.html',{'form':form})


def project_edit(requests,pid):
    if requests.method == "POST":
        form = ProjectEditForm(requests.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            fund = form.cleaned_data['fund']
            sys = form.cleaned_data['sys']
            type = form.cleaned_data['type']
            version = form.cleaned_data['version']
            p = tels.objects.get(id=pid)
            p.name = name
            p.fund = fund
            p.sys = sys
            p.type = type
            p.version = version
            p.save()
        return HttpResponseRedirect("/project/")
    else:
        if pid:
            p = tels.objects.get(id = pid)
            form = ProjectEditForm(instance = p)
        else:
            form = ProjectForm()
        return render(requests, 'project_edit.html', {'form': form,'id':pid})



def project_delete(requests,pid):
    if requests.method == "GET":
        p = tels.objects.get(id=pid)
        p.delete()
        return HttpResponseRedirect("/project/")
    else:
        return HttpResponseRedirect("/project/")


def project_search(requests):
    name = requests.GET.get('name')
    sys = requests.GET.get('sys')
    search_dict = dict()
    if name:
        search_dict["name"] = name
    if sys:
        search_dict["sys"] = sys

    #projects = tels.objects.filter(name__icontains=name_q)

    # projects其实就是all_search_data
    projects = tels.objects.filter(**search_dict)
    return render(requests, 'project_list.html', {'projects': projects})




