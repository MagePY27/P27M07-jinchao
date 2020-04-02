from django.shortcuts import render
#导入http模版，前端显示格式
from django.http import HttpResponse,QueryDict
from django.shortcuts import render
from hello.models import User


#接收到用户访问请求 把数据库数据传到对应的初始列表html文件
def list(request):
    users = User.objects.all()
    return render(request, 'hello/userlist.html', {"users": users})

#接收到用户新增请求 转收集数据的usernew的html文件
def usernew(request):
    return render(request, 'hello/usernew.html')
#接受到用户新增的数据，将其同步到数据库 并返回到初始页面
def usernew_ok(request):
    if request.method == 'POST':
        add = request.POST.dict()
        User.objects.create(**add)
    users = User.objects.all()
    return render(request, 'hello/userlist.html', {"users": users})

#接受到用户删除指令时删除相关数据并返回初始界面（这里想做成弹框确认，还未掌握相关html知识）
def userdel(request,udel):
    User.objects.get(id=udel).delete()
    users = User.objects.all()
    return render(request, 'hello/userlist.html', {"users": users})

#接收到用户修改请求后 转到收集修改信息界面
def usermod(request,umod):
    user = User.objects.get(id=umod);
    return render(request, 'hello/usermod.html', {"user": user})
#接收到用户确认修改请求后 对数据库进行同步 并返回初始界面
def usermod_ok(request):
    if request.method == 'POST':
        postget = request.POST.dict()
        User.objects.filter(id=request.POST.get('id')).update(**postget)
    users = User.objects.all()
    return render(request, 'hello/userlist.html', {"users": users})









#####   练习函数 #######
def index(request):
    #直接交给模版文件
    return render(request,'hello/hello.html',)
def test(request):
    testname = "testest"  ###添加一个变量 要把这个变量里面的内容传到前端显示
    name = ['tom', 'bob','pop']          ##列表形式
    user = {'name': 'tom', 'age':'18'}  ##字典格式
###嵌套格式 列表内嵌套字典
    userlist = [
        {'username':'tom','age':18},
        {'username':'bob','age':19},
        {'username':'pop','age':22},
    ]
    return render(request,'hello/hello.html',{"testhtm":testname,'name':name,'user':user,'userlist':userlist})   ###把数据封装成字典传入前端
# def index(request):
#     classname = "DevOps"
#     books = ['Python', 'Java', 'Django']
#     user = {'name': 'kk', 'age': 18}
#     userlist = [{'name': 'kk', 'age': 18}, {'name': 'rock', 'age': 19},
#                 {'name': 'mage', 'age': 20}]
#     return render(request, 'hello/hello.html')
#请求参数接收，默认为get请求，通过method判断POST请求
# def index(request):
#     #2020 88  为缺省值 建议设置 不设置没有传参会报错
#     data = request.GET
#     year = data.get("year","8888")
#     month = data.get("month","88")
#     if request.method == "POST":
#         data = request.POST
#         year = data.get("year","6666")
#         month = data.get("month", "66")
#     return HttpResponse("year is %s,month is %s" % (year,month) )
#
#位置传参
def Location(request,year,month):
    return HttpResponse('year is {},month is {} '.format(year,month) )
#关键字传参
def keywords(request,**kwargs):
    year = kwargs.get('year',2022)
    month = kwargs.get('month',9)
    return HttpResponse('year is {},month is {} '.format(year,month) )
# Create your views here.
