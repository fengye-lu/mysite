from django.shortcuts import render, HttpResponse, redirect
from blog import models
# Create your views here.
import datetime

def cur_time(request): # request表示请求的信息，相当于environ
    times = datetime.datetime.now()
    # return HttpResponse("<h1 style='color:red'>ok!</h1>")
    return render(request, 'cur_time.html', {'abc':times}) # 相对于HttpResponse多了一步渲染
    # 但底部还是调用的HttpResponse

def userInfo(req):
    if req.method == 'POST':
        u = req.POST.get('username', None)
        s = req.POST.get('sex', None)
        e = req.POST.get('email', None)
        # user = {'username':username, 'sex':sex, 'email':email}
        # user_list.append(user)

        models.UserInfo.objects.create(
            username=u,
            sex=s,
            email=e,
        )
    user_list = models.UserInfo.objects.all()

    # return render(req, 'index.html', {'user_list':user_list})
    return render(req, 'index.html', locals()) # 用locals取得本地变量
    # return redirect('/cur_time') # 跳转页面


def year_archive(req):
    return HttpResponse('year')

def year_archives(req,month,year):  # 从urls有多少值传进来就用多少变量去接收
    return HttpResponse(year+'year'+month)

def index(req):
    if req.method == 'POST':
        username = req.POST.get('user')
        password = req.POST.get('pwd')

        if username=='fengye' and password=='123':
            return HttpResponse('登录成功！')

    return render(req, 'login.html')


def introduce(req):
    return HttpResponse('ok!')


def login(req):
    if req.method == 'POST':
        if 1 :
            return redirect('/blog/home')
    return render(req,'login.html')

def home(req):
    name = 'jackey'
    return render(req, 'home.html', {'name':name})
