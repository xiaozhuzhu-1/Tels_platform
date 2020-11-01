"""one_Platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app_persion import views as persion_views
from app_DataSelect import views

from telephone_manage import views as manage_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 个人中心
    path('',persion_views.login),
    path('login/',persion_views.login),
    path('logout/',persion_views.logout),

    # 管理中心
    #path('manage/',manage_views.manage),

    path('project/',include('telephone_manage.urls')),
    path('select/',include('app_DataSelect.urls')),






]
