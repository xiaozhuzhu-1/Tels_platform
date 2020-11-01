from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect    # 重定向方法
from django.contrib import auth    # 认证模块，账号密码校验
from django.contrib.auth.decorators import login_required   # 装饰登录状态的视图，在函数前@login_required即可
# Create your views here.
# 用来写请求的处理逻辑的

def login(requests):
    # 返回登录页面
    if requests.method == "GET":
        return render(requests,"login.html")

    # 点击登录按钮的判断
    if requests.method =="POST":

        # 前端传进来的json格式数据都在函数的入参 requests。可通过函数得到其中想要的
        username = requests.POST.get("username","")
        password = requests.POST.get("password","")

        # 调试问题使用，在启动django的终端窗口上会打印出来
        # print("==>name",username)
        # print("==>passwd",password)

        if username == "" or password == "":
            return render(requests, "login.html",{"error":"用户名或密码为空！"})

        # 其中左边的变量username、password是从sqlite3数据库里面取的
        user = auth.authenticate(username=username,password=password)
        # print("用户是否存在",user)  #不存在返回none，存在返回name
        if user is not None :
            auth.login(requests,user)   # 记录用户的登录状态，在数据库新增一个seesion
            return HttpResponseRedirect("/project/")    # 重定向，后端也可发起一个路径请求
        else:
            return render(requests, "login.html", {"error": "用户名或密码错误！！！"})

# 退出功能后，会自动清掉seesion,然后返回根目录指向登录页
def logout(requests):
    auth.logout(requests)
    return HttpResponseRedirect("/")