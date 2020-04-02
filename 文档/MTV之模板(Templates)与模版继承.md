# MTV之模版（Templates）
- `简单说就是将数据通过web展现给用户，而不是单纯的文本`
~~~
用户通过URL发起的各种请求，我们都可以通过View中定义的处理方法返回给相应的数据。但是返回给用户的界面体验太差，这个时候模板就该出场了
模板主要负责将视图返回的数据渲染到页面，更加优雅的展示给用户
~~~

### 1、使用模版
1. 全局配置，配置全局文件setting.py
~~~
# cat devops/settings.py  |grep TEMPLATES  -A 14
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', #默认模版引擎，后续再参考不同引擎
        'DIRS': [BASE_DIR+"/templates"],                            #dir 路径存放位置 你想要渲染一个数据要通过一个文件来渲染 这里配置对应html文件路径
        'APP_DIRS': True,                                             #Trur打开 就是工程目录下寻找templates，如果找不到就在各应用app下继续寻找 建议打开 有些项目可能会把html放到app本身路径
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
~~~

2. 创建公共模版templates目录
~~~
# mkdir -p templates/hello
# tree templates
templates
└── hello

1 directory, 0 files
~~~
3. 配置简单url
~~~
cat hello/urls.py 
from django.urls import path,re_path
from . import views

app_name = 'hello'
urlpatterns = [
    path('hello/',views.index,name='index'),

]
~~~

4. 编写view，模拟Django常用数据类型，并传给模版
~~~
# cat hello/views.py 
from django.shortcuts import render
#导入http模版，前端显示格式
from django.http import HttpResponse,QueryDict

def index(request):
    #直接交给模版文件
    return render(request, 'hello/hello.html')
~~~
5. 编写hello.html文件
~~~
# cat templates/hello/hello.html 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<body>
<p> hello Django</p>

</body>
</body>
</html>
~~~
![MTV模版打通效果图](G:\python实战\python实战练习\通过模版访问.png)
6. 为 html 简单给文字加一个背景色
~~~
# cat templates/hello/hello.html 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<body>
<p style="background-color: blue">
    hello Django
</p>
<p style="background-color: red">
    hello word
</p>

</body>
</body>
</html>
~~~ 
![MTV模版打通效果图](G:\python实战\python实战练习\MTV模版打通效果图.png)

### 2. 数据传输
1. 将相关数据传输到前台显示（列表，字典，嵌套形式等）
2. 界面for 循环取值
3. 初始配置
   * 定义url 主url继续使用上次配置好的 无需改变，应用URL设计
~~~
# cat hello/urls.py 
from django.urls import path,re_path
from . import views

app_name = 'hello'
urlpatterns = [
    path('test/',views.test,name='test'),

~~~

   * 编写对应url的view，来处理用户的请求
~~~
# cat hello/views.py 
from django.shortcuts import render
#导入http模版，前端显示格式
from django.http import HttpResponse,QueryDict
from django.shortcuts import render

def index(request):
    #直接交给模版文件
    return render(request,'hello/hello.html',)
def test(request):
    testname = "testest"            ###添加一个变量 要把这个变量里面的内容传到前端显示
    return render(request,'hello/hello.html',{"testhtm":testname})   ###把数据传入前端，将变量交给前端 testhtm相当于交给前端的名称

~~~
   * 编写hello.html文件 将接收传过来的变量数据testhtm 写入html文件
~~~
# cat templates/hello/hello.html 
<html >
<head>
    <title> 测试</title>
</head>>
<body>
<p style="background-color: blue">
    hello Django </p>
<p style="background-color: #ffb536">
    hello word </p>
<p>{{ testhtm }}</p>>     

</body>
</html>
~~~
   * web访问http://192.168.0.120:8000/hhhhh/test/
~~~
http://192.168.0.120:8000/hhhhh/test/

得到以下显示
>

hello Django

hello word

testest
> 

~~~
   * 至此 我们可以将后台的变量数据传输到前台显示
4. 将list，dict 嵌套形式等数据 传输到前台显示
	* 编写对应的view函数
~~~
# cat hello/views.py 
from django.shortcuts import render
#导入http模版，前端显示格式
from django.http import HttpResponse,QueryDict
from django.shortcuts import render

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
~~~
   * 编辑hello.html文件接收数据 （前端html格式编写不清楚后续补充相关知识，先了解前后端关系）
~~~
# cat templates/hello/hello.html 
<html >
<head>
    <title> 测试</title>
</head>
<body>
<p style="background-color: blue">
    hello Django     </p>
<p style="background-color: #ffb536">
    hello word        </p>
<p>{{ testhtm }}</p>
<!--取列表数据-->
<li>{{ name.0 }} </li>
<li>{{ name.1 }} </li>
<li>{{ name.2 }} </li>
<!--取字典数据-->
<li> my name is {{user.name}} my age is {{user.age}}</li>
<!--for循环取嵌套数据-->
{% for user in userlist %}
<li>{{user.username}} is {{user.age}}</li>
{% endfor %}

</body>
</html>
~~~
访问http://192.168.0.120:8000/hhhhh/test/ 得到相关数据展示
![获取数据](G:\python实战\python实战练习\获取数据.jpg)

##### 这样我们就初步掌握了 如何将后台数据通过变量形式传输到前端

### 模版使用
1. template模版集成化——简化代码
	* Django 使用了“模版继承”的概念，模版继承让你在模版使用中减少了冗余内容：
	* 每一个模版只需要定义它独特的部分即可 
	* 相当于面向对象中类的继承，公用的东西公用，自己的东西自己改
2. 例如常见的网址布局，基本框架，周边都是相同不变，我们把公共不变的地方抽出来作为公共模版，各个子页面继承模版直接引用公共部分，同时对需要改变的部分进行重写。这种设计与面向对象中类的设计很相似 使代码最大程度的复用，并且使得添加内容更加简单。
3. 实际操作
	* 用户需求模拟
~~~
		用户访问http：//192.138.0.120/hhhhh/list 返回一个用户列表，以表格形式呈现
~~~
4. 相关配置 
* 主路由不需要管 配置应用路由 
~~~
# cat hello/urls.py 
from django.urls import path,re_path
from . import views

app_name = 'hello'
urlpatterns = [
    path('list/',views.list,name='list'),
~~~
* 配置views函数
~~~
# cat hello/views.py 
from django.shortcuts import render
#导入http模版，前端显示格式
from django.http import HttpResponse,QueryDict
from django.shortcuts import render


def list(request):
    ##相关列表数据，类比数据库取到的数据后续可以直接在数据库取
    users = [
        {'username': 'user1', 'name_cn': 'tom', 'age': 18},
        {'username': 'user2', 'name_cn': 'bob', 'age': 19},
        {'username': 'user3', 'name_cn': 'pop', 'age': 20},
    ]
    #新添加一个users.html文件用于测试
    return render(request, 'hello/users.html', {"users": users})
~~~
* 新建一个users.html文件用于显示测试
~~~
# cat templates/hello/users.html 
<html>
<head>
<title>自动化运维平台</title>
</head>
<body>
<!-- 每个?页?面都有个标题且样式基本不不会变，可以抽象出来。变的标题内容做成变量量 -->
<p style="background-color: #57ff2e;">测试模版先套用即可</p>
<p style="background-color:yellow;">用户列表</p>
<!-- ?页?面都内容往往是变化的这?一块，做成变量量即可 -->
<table border="1">
<thead>
<tr>
<th>用户名</th>
<th>姓名</th>
<th>年龄</th>
</tr>
</thead>
<tbody>
{% for user in users %}
<tr>
<td>{{ user.username }}</td>
<td>{{ user.name_cn }}</td>
<td>{{ user.age }}</td>
</tr>
{% endfor %}
</tbody>
</table>
<!-- 每个页面都有个底部且样式基本不不会变，可以抽象出来 -->
<p style="background-color:red;">版权所有：马哥教育</p>
</body>
</html>
~~~
* 访问http://192.168.0.120:8000/hhhhh/list/  得到下图数据

![列表界面](G:\python实战\python实战练习\列表界面.jpg)

### 模版继承
   * 定义url
~~~
# cat hello/urls.py 
from django.urls import path,re_path
from . import views

app_name = 'hello'
urlpatterns = [
    path('list/',views.list,name='list'),
~~~
* 编写对应的view来处理相关用户请求

~~~
# cat hello/views.py 
from django.shortcuts import render
#导入http模版，前端显示格式
from django.http import HttpResponse,QueryDict
from django.shortcuts import render


def list(request):
    ##相关列表数据，类比数据库取到的数据后续可以直接在数据库取
    users = [
        {'username': 'user1', 'name_cn': 'tom', 'age': 18},
        {'username': 'user2', 'name_cn': 'bob', 'age': 19},
        {'username': 'user3', 'name_cn': 'pop', 'age': 20},
    ]
    #新添加一个list.html文件用于测试
    return render(request, 'hello/list.html', {"users": users})
~~~
* 编写template文件 
   * 定义母版，母版里面是公用部分 html文件 
   * `我们用 {% block title %｝来开始定义变量 title为变量名 用{% endblock %}` 来结束定义变量`
   * `{% block 变量名 %} 变量 {% endblock %}`
~~~
# cat templates/base.html 
<html>
<head>
<title>自动化运维平台</title>
</head>
<body>
<!-- 每个页面都有个标题且样式基本不会变，可以抽象出来。变的标题内容做成变量 -->
<p style="background-color:yellow;">
{% block title %} 用户列表 {% endblock %}
</p>
<!-- 页面的内容往往是变化的这一块，做成变量即可 -->
{% block content %}
{% endblock %}
<!-- 每个页面都有个底部且样式基本不会变，可以抽象出来 -->
<p style="background-color:red;">版权所有：马哥教育</p>
</body>
</html>

~~~
   * 继承母版 子页面继承
~~~
# cat templates/hello/list.html 
{% extends "base.html" %}

~~~
   * 仅继承时 我们访问web 查看结果图 
	 ![仅继承母版](G:\python实战\python实战练习\png\仅继承母版.jpg)
  *  重写母版变化部分 
~~~
# cat templates/hello/list.html 
{% extends "base.html" %}

{% block title %} 用户的列表 {% endblock %}

{% block content %}
<table border="1">
<thead>
    <tr>
        <th>用户名</th>
        <th>姓名</th>
        <th>年龄</th>
    </tr>
</thead>
<tbody>
    {% for user in users %}
    <tr>
        <td>{{ user.username }}</td>
        <td>{{ user.name_cn }}</td>
        <td>{{ user.age }}</td>
    </tr>
    {% endfor %}
</tbody>
</table>
{% endblock %}
~~~



















