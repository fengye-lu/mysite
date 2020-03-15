from django.shortcuts import render, HttpResponse, redirect
from blog import models
from django.db.models import Avg, Min, Sum, Max
from django.http import JsonResponse
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
        y = req.POST.get('year', None)

        # user = {'username':username, 'sex':sex, 'email':email}
        # user_list.append(user)

        # 增
        models.UserInfo.objects.create(
            username=u,
            sex=s,
            email=e,
            year=y,
        )
        '''  create传值的方式二，用字典的形式
                models.UserInfo.objects.create(
            **{
                'username':u,
                'sex':s,
                'email':e,
                'year':y,
            }
        )
        '''

    user_list = models.UserInfo.objects.all()

    # obj = models.UserInfo.objects.filter(id__in=[1, 3, 6, 7])
    # print(obj[0].username)

    # models.UserInfo.objects.filter(id=4).update(username='jackey',sex='diddle',email='dsds',year=3)

    # obj = models.UserInfo.objects.filter(id=2)
    # print(obj.values('sex'))
    # print(obj.query)  # 显示实现数据库操作的sql语句

    print(models.UserInfo.objects.all().aggregate(Avg('year')))



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
