# WEB框架的设计逻辑MVC&&MTV
### 一、用户输入网址回车后都发生了什么？
~~~
   从用户角度分析Django框架（网站）都需要哪些零件？经典的MVC(MTV)框架是怎么来的？
~~~

   * 用户输入网址请求数据<-->路由/url（路标：定义用户输入的网址接下来交给谁处理）。Django中通过urls.py文件来维护路由--> 处理器的对应关系（原则来讲通过主路由交给处理器处理数据，主路由也可以交给其他路由来处理但最终经过路由都会转到处理器view）
   * 用户请求的数据谁来处理，怎么处理？ <-->view(控制器/处理器)。用户请求的网址最终会被路由（urls）指向对应的控制器来处理。Django中通过viwes.py文件定义处理逻辑，对数据进行处理。
   * 用户想要的数据存放在哪里？<-->model(模型)。结构化的存储用户需要数据，控制器处理后的数据存储在model，用户需要数据时，控制器再骂出来加工返回给用户。Django中的model.py 中定义了模型（也就是数据表结构，*简单说就是存与取数据的地方，用户取数据来这里拿，输入的数据也从这里取*）
   * 用户如何看到自己想要的数据？<-->template（模版）。模版负责将views处理器处理好的数据（一般被转换成list、dict、json）渲染成用户能看的明白的格式，即在html中展现处理好的数据（*简单说就是将程序处理好的数据交给前端界面显示，这里如果有充分的前端技术可以做的非常漂亮，如果没有的话也可以套用模版来输出，或者在网上扒一些别人好看的模版换上自己的内容，相当于把数据穿上衣服，我们来为数据挑选好看的衣服*）
	* 流程图如下
	![流程图](G:\python实战\python实战练习\流程图.png)
	 
### 二、认识Django结构，分析Django框架
~~~
分析Django结构，连接前后端
~~~
   1. 分析工程目录（之前我们创建的devops工程目录）
~~~
# tree devops/
devops/
├── __init__.py					 	###初始化文件，表明这是一个包
├── __pycache__					 	
│   ├── __init__.cpython-36.pyc		
│   ├── settings.cpython-36.pyc		
│   ├── urls.cpython-36.pyc			
│   └── wsgi.cpython-36.pyc			
├── settings.py						###工程整体主配置文件 
├── urls.py							###工程主路由，定义路由路径
└── wsgi.py							###工程web服务器入口（nginx/apache）
~~~
   2. 分析app（应用）目录（我们之前创建的hello应用）
~~~
# tree hello/
hello/
├── admin.py							##后台管理文件
├── apps.py							##app命名文件（工程主配置文件会配置这里的数据）
├── __init__.py						##初始化文件，默认为空
├── migrations						##数据迁移文件
│   ├── __init__.py
│   └── __pycache__
│       └── __init__.cpython-36.pyc
├── models.py						##模型文件
├── __pycache__						##可以理解成运行一次后，后续调用模块不改变情况下加快启动的文件	
│   ├── admin.cpython-36.pyc
│   ├── apps.cpython-36.pyc
│   ├── __init__.cpython-36.pyc
│   ├── models.cpython-36.pyc
│   ├── urls.cpython-36.pyc
│   └── views.cpython-36.pyc
├── tests.py
├── urls.py							##定义路由，默认没有，自行添加
└── views.py							##逻辑处理，控制器
~~~
   3. 在全局配置文件中注册新创建的app
	  *  在这里看你的app信息
~~~
# cat hello/apps.py 
from django.apps import AppConfig


class HelloConfig(AppConfig):
    name = 'hello'
~~~ 	
4. * 在全局配置文件中注册 
~~~
# cat devops/settings.py |grep INSTALLED_APPS  -A 9
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello.apps.HelloConfig'   				###这里配置对应的应用apps.py的信息，配置了这里，主工程就可以找到应用了
]
~~~
5.   * 编写主url路径使用户能够找到对应的数据
~~~
# cat devops/urls.py
from django.contrib import admin
from django.urls import path,re_path
from hello import views						#从hello（我们之前创建了的目录）中调用views.py文件，这个里面会写对应的函数index
from django.urls import path,include		#导入include url转向
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('hello/',views.index),				#当用户url填写hello会直接调用对应的函数处理
    path('hhhhh/',include('hello.urls'))	#访问hhhhh将url转给应用hello自己的urls处理
]

~~~

6.   * 编写应用自己的url路径 
~~~
# cat hello/urls.py 
from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path('(?P<year>[0-9]{4})/(?<month>[0-9]{2})',views.index,name='index'),
#当接到主url后转到自身url，拼接自身url后便是客户访问的url，不通的url路由对应处理器不同的逻辑函数
    path('cpu/',views.cpu,name='index'),
    path('free/',views.free,name='index'),
    path('ip/',views.ip,name='index'),
    path('ping/',views.ping,name='index'),

]
~~~
7.   * 上面路由已经指向了处理器，那么接下来我们为处理器编写相关逻辑
~~~
# cat hello/views.py 
from django.shortcuts import render
from django.http import HttpResponse


###当用户输入hello路由（ip:8000/hello)时，会由主路由直接调用views的index函数 
def index(request):
    return HttpResponse("<p>hello world,hello,django</p>")
###当用户输入hhhhh路由（ip:8000/hello/***）时,会由主路由转到应用自身路由，自身路由拼接应用自身路由后返回对应不同的函数
def cpu(request):
    return HttpResponse("<p>'mycpu is 88% </p>")
def ip(request):
    return HttpResponse("<p>'ip: 192.168.0.120 </p>")
def free(request):
    return HttpResponse("<p>'free is 50%</p>")
def ping(request):
    return HttpResponse("<p>'192.168.0.120‘s ping OK'</p>")

~~~
8.   * 通过以上设计 就可以访问web界面来得到我们简单的数据了
### 三、MTV视图（url&&view）
~~~
通过上面的url设计，我们走通了前端到后端的连接，能将后端数据表现到界面上，那么接下来要处理用户不同请求读与写（get/post） 
~~~

   1.  request && response
~~~
	1. request —— 用户有两大类，五小类对服务器发起请求
		- get请求
			- 不带参数										 #1种
			- 带参数										
				-  ？参数      -- url						 #2种
				-  位置参数    -- url设计					 #3种
				-  关键字参数  -- url设计 					 #4种
	    - post 请求（正常情况下都会带参数）常用语表单场景 	 #5种
~~~
  2. response —— 2大类3小类获取到数据
~~~
		* request.method  —— 判断请求的方式 
		* request.body —— 第一种获取数据的方法
			* print(type(request.body)) # byte
			* print(QueryDict(request.body)) # QueryDict
			* print(QueryDict(request.body).dict) # dict
		* request.GET # 第2种方式获取GET QueryDict 
 			* request.GET.get('name','devops') 
		* request.POST # 第2种获取post数据方式 <QueryDict: {'year':['2019']
			* request.POST.getlist（'id'）
		*  kwargs.get('year', 2020) # 第三种获取GET 只适?关键字请求的数据
   3.  不带参数的读 ——get
		* 用户请求带参数的url
			* 之前已经配置的简单的url设计访问http://192.168.0.120:8000/hhhhh/ 得到index函数返回结果

~~~
3. 参考之前app应用 cat hello/urls.py 
~~~
from django.urls import path,re_path
from . import views

urlpatterns = [
    #re_path('(?P<year>[0-9]{4})/(?<month>[0-9]{2})',views.index,name='index'),
#当接到主url后转到自身url，拼接自身url后便是客户访问的url
    path('',views.index,name='index'),			###当访问为空的时候调用index函数
    path('cpu/',views.cpu,name='index'),
    path('free/',views.free,name='index'),
    path('ip/',views.ip,name='index'),
    path('ping/',views.ping,name='index'),

]


# cat hello/views.py 
from django.shortcuts import render
#导入http模版，前端显示格式
from django.http import HttpResponse


#定义index函数，由路由指向
def index(request):
    return HttpResponse("<p> hello Djang </p> ")

def cpu(request):
    return HttpResponse("<p>'mycpu is 88% </p>")
def ip(request):
    return HttpResponse("<p>'ip: 192.168.0.120 </p>")
def free(request):
    return HttpResponse("<p>'free is 50%</p>")
def ping(request):
    return HttpResponse("<p>'192.168.0.120‘s ping OK'</p>")

~~~              
4. 带参数的读 —— get
   1. 用户请求带参数的url
~~~
		有三种场景
			1、普通参数
				http://192.168.0.120:8000/hhhhh/?year=2019&month=06
			2、位置参数
				http：// 192.168.0.120://hhhhh/2019/06
			3、关键字传参
			    http：// 192.168.0.120://hhhhh/2019/06
~~~	
5. 配置views.py文件，对应开启不同的url测试
~~~
###配置views.py文件 
# cat hello/views.py 
from django.shortcuts import render
#导入http模版，前端显示格式
from django.http import HttpResponse

#普通参数接受
def index(request):
    #2020 88  为缺省值 建议设置 不设置没有传参会报错
    year = request.GET.get('year','2020')
    month = request.GET.get('month','88')
    return HttpResponse("year is %s,month is %s" % (year,month) )
#位置传参
def Location(request,year,month):
    return HttpResponse('year is {},month is {} '.format(year,month) )
#关键字传参
def keywords(request,**kwargs):
    year = kwargs.get('year',2022)
    month = kwargs.get('month',9)
    return HttpResponse('year is {},month is {} '.format(year,month) )
# Create your views here.
			
~~~
6. 配置对应url文件
   1. 普通接收参数
~~~
###普通参数
# cat hello/urls.py 
from django.urls import path,re_path
from . import views

urlpatterns = [
#当接到主url后转到自身url，拼接自身url后便是客户访问的url
#普通url 和无参数url类似    
    path('',views.index,name='index'),
#位置匹配
#    re_path("([0-9]{4})/([0-9]{2})",views.Location,name='Location'),

]

###访问对应url 不输入参数数据时默认为缺省值
http://192.168.0.120:8000/hhhhh/
year is 2020,month is 88
传入参数，需要对应名称如果只传入一个参数则另一个参数使用缺省值
http://192.168.0.120:8000/hhhhh/?year=2222&month=11
year is 2222,month is 11
~~~
   2. 位置传参 
~~~
* cat hello/urls.py 
from django.urls import path,re_path
from . import views

urlpatterns = [
#当接到主url后转到自身url，拼接自身url后便是客户访问的url
#普通url 和无参数url类似    
#    path('',views.index,name='index'),
#位置匹配
    re_path("([0-9]{4})/([0-9]{2})",views.Location,name='Location'),
#关键字匹配
#re_path("(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/",views.keywords,name='keywords'),
]


http://192.168.0.120:8000/hhhhh/1444/44
year is 1444,month is 44
~~~
   3. 关键字传参 在url时就规定了关键字，避免了参数错传
~~~
# cat hello/urls.py 
from django.urls import path,re_path
from . import views

urlpatterns = [
#当接到主url后转到自身url，拼接自身url后便是客户访问的url
#普通url 和无参数url类似    
#    path('',views.index,name='index'),
#位置匹配
#    re_path("([0-9]{4})/([0-9]{2})",views.Location,name='Location'),
#关键字匹配
    re_path("(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/",views.keywords,name='keywords'),
]

http://192.168.0.120:8000/hhhhh/5555/11/
year is 5555,month is 11 

~~~	
7. 带参数的写——post （关于get请求，不传参数就是读取相关默认的缺省值，如果传入参数就相当于读取字典的value值）
	* 设置接触url
~~~
# vim hello/urls.py 

from django.urls import path,re_path
from . import views

urlpatterns = [
    path('hello/',views.index,name='index'),
~~~
   * 设置对应的处理器
~~~
# cat hello/views.py 
from django.shortcuts import render
#导入http模版，前端显示格式
from django.http import HttpResponse,QueryDict

#请求参数接收，默认为get请求，通过method判断POST请求
###我们接到用户传过来的request信息有很多，通过不同的参数查看相关信息
def index(request):
    print(request.scheme)	###http 不常用
    print(request.method)	###类型查看用户发过来的是什么类型 分别做相关处理例如 GET、POST、delete put
    print(request.headers)	###我们常说的head头部信息
    print(request.path)		###path 路径 url信息
    print(request.META)		###我们常说的Header信息，里面包含了很多信息，用户地址 服务器地址等信息，可以看到哪个用户访问你 
    print(request.GET)		###QueryDict类型，简单说就是python给我们的get请求封装成字典类型，以方便我们提取数据 
    data = request.GET
    year = data.get("year","8888")
    month = data.get("month","88")
    if request.method == "POST":  ###通过method 判断是get还是post请求
#        print(request.method)	  #打印类型
#        print(request.body)	  #body信息
#        print(QueryDict(request.body).dict()) ##大一数据内容
#        print(request.POST)	
        data = request.POST			#python已经将数据封装好了POST 可以直接在POST里get取相关数据
        year = data.get("year","6666")
        month = data.get("month", "66")
    return HttpResponse("year is %s,month is %s" % (year,month) )
~~~
   * 通过web界面来获取get请求的数据 使用缺省值方便对比post
~~~
	http://192.168.0.120:8000/hhhhh/hello/
  * 返回信息
	year is 8888,month is 88
~~~
   * 通过curl模拟请求
~~~
	#curl -X POST http://192.168.0.120:8000/hhhhh/hello/ -d 'year=2020&month=22'
	year is 2020,month is 22
	* 通过curl请求缺省值
	#curl -X POST http://192.168.0.120:8000/hhhhh/hello/ -d ''
	year is 6666,month is 66
	* 至此我们可以看到 当采用缺省值时 采用的返回信息不同 一次证明区分了 get和post请求 以此我们便可以对get与post请求做分别的处理器view处理 
~~~
   * 如果curl post报错可能是安全验证的问题 可以把安全验证关闭 工程的setting文件配置
~~~
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

~~~

###   总结
* 了解用户的不同请求数据 get还是post
* 默认request是get请求 通过request.method 来判断是否是post请求
* QueryDict python为我们做的优化处理 由于前端与后端语言不通 Django把前端数据转化为了我们方便处理的dict数据
* 主要通过 request.GET.get 与request.HOST.get 来获取相关数据 并处理











		

		
