# MTV֮ģ�棨Templates��
- `��˵���ǽ�����ͨ��webչ�ָ��û��������ǵ������ı�`
~~~
�û�ͨ��URL����ĸ����������Ƕ�����ͨ��View�ж���Ĵ��������ظ���Ӧ�����ݡ����Ƿ��ظ��û��Ľ�������̫����ʱ��ģ��͸ó�����
ģ����Ҫ������ͼ���ص�������Ⱦ��ҳ�棬�������ŵ�չʾ���û�
~~~

### 1��ʹ��ģ��
1. ȫ�����ã�����ȫ���ļ�setting.py
~~~
# cat devops/settings.py  |grep TEMPLATES  -A 14
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', #Ĭ��ģ�����棬�����ٲο���ͬ����
        'DIRS': [BASE_DIR+"/templates"],                            #dir ·�����λ�� ����Ҫ��Ⱦһ������Ҫͨ��һ���ļ�����Ⱦ �������ö�Ӧhtml�ļ�·��
        'APP_DIRS': True,                                             #Trur�� ���ǹ���Ŀ¼��Ѱ��templates������Ҳ������ڸ�Ӧ��app�¼���Ѱ�� ����� ��Щ��Ŀ���ܻ��html�ŵ�app����·��
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

2. ��������ģ��templatesĿ¼
~~~
# mkdir -p templates/hello
# tree templates
templates
������ hello

1 directory, 0 files
~~~
3. ���ü�url
~~~
cat hello/urls.py 
from django.urls import path,re_path
from . import views

app_name = 'hello'
urlpatterns = [
    path('hello/',views.index,name='index'),

]
~~~

4. ��дview��ģ��Django�����������ͣ�������ģ��
~~~
# cat hello/views.py 
from django.shortcuts import render
#����httpģ�棬ǰ����ʾ��ʽ
from django.http import HttpResponse,QueryDict

def index(request):
    #ֱ�ӽ���ģ���ļ�
    return render(request, 'hello/hello.html')
~~~
5. ��дhello.html�ļ�
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
![MTVģ���ͨЧ��ͼ](G:\pythonʵս\pythonʵս��ϰ\ͨ��ģ�����.png)
6. Ϊ html �򵥸����ּ�һ������ɫ
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
![MTVģ���ͨЧ��ͼ](G:\pythonʵս\pythonʵս��ϰ\MTVģ���ͨЧ��ͼ.png)

### 2. ���ݴ���
1. ��������ݴ��䵽ǰ̨��ʾ���б��ֵ䣬Ƕ����ʽ�ȣ�
2. ����for ѭ��ȡֵ
3. ��ʼ����
   * ����url ��url����ʹ���ϴ����úõ� ����ı䣬Ӧ��URL���
~~~
# cat hello/urls.py 
from django.urls import path,re_path
from . import views

app_name = 'hello'
urlpatterns = [
    path('test/',views.test,name='test'),

~~~

   * ��д��Ӧurl��view���������û�������
~~~
# cat hello/views.py 
from django.shortcuts import render
#����httpģ�棬ǰ����ʾ��ʽ
from django.http import HttpResponse,QueryDict
from django.shortcuts import render

def index(request):
    #ֱ�ӽ���ģ���ļ�
    return render(request,'hello/hello.html',)
def test(request):
    testname = "testest"            ###���һ������ Ҫ�����������������ݴ���ǰ����ʾ
    return render(request,'hello/hello.html',{"testhtm":testname})   ###�����ݴ���ǰ�ˣ�����������ǰ�� testhtm�൱�ڽ���ǰ�˵�����

~~~
   * ��дhello.html�ļ� �����մ������ı�������testhtm д��html�ļ�
~~~
# cat templates/hello/hello.html 
<html >
<head>
    <title> ����</title>
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
   * web����http://192.168.0.120:8000/hhhhh/test/
~~~
http://192.168.0.120:8000/hhhhh/test/

�õ�������ʾ
>

hello Django

hello word

testest
> 

~~~
   * ���� ���ǿ��Խ���̨�ı������ݴ��䵽ǰ̨��ʾ
4. ��list��dict Ƕ����ʽ������ ���䵽ǰ̨��ʾ
	* ��д��Ӧ��view����
~~~
# cat hello/views.py 
from django.shortcuts import render
#����httpģ�棬ǰ����ʾ��ʽ
from django.http import HttpResponse,QueryDict
from django.shortcuts import render

def index(request):
    #ֱ�ӽ���ģ���ļ�
    return render(request,'hello/hello.html',)
def test(request):
    testname = "testest"  ###���һ������ Ҫ�����������������ݴ���ǰ����ʾ
    name = ['tom', 'bob','pop']          ##�б���ʽ
    user = {'name': 'tom', 'age':'18'}  ##�ֵ��ʽ
###Ƕ�׸�ʽ �б���Ƕ���ֵ�
    userlist = [
        {'username':'tom','age':18},
        {'username':'bob','age':19},
        {'username':'pop','age':22},
    ]
    return render(request,'hello/hello.html',{"testhtm":testname,'name':name,'user':user,'userlist':userlist})   ###�����ݷ�װ���ֵ䴫��ǰ��
~~~
   * �༭hello.html�ļ��������� ��ǰ��html��ʽ��д����������������֪ʶ�����˽�ǰ��˹�ϵ��
~~~
# cat templates/hello/hello.html 
<html >
<head>
    <title> ����</title>
</head>
<body>
<p style="background-color: blue">
    hello Django     </p>
<p style="background-color: #ffb536">
    hello word        </p>
<p>{{ testhtm }}</p>
<!--ȡ�б�����-->
<li>{{ name.0 }} </li>
<li>{{ name.1 }} </li>
<li>{{ name.2 }} </li>
<!--ȡ�ֵ�����-->
<li> my name is {{user.name}} my age is {{user.age}}</li>
<!--forѭ��ȡǶ������-->
{% for user in userlist %}
<li>{{user.username}} is {{user.age}}</li>
{% endfor %}

</body>
</html>
~~~
����http://192.168.0.120:8000/hhhhh/test/ �õ��������չʾ
![��ȡ����](G:\pythonʵս\pythonʵս��ϰ\��ȡ����.jpg)

##### �������Ǿͳ��������� ��ν���̨����ͨ��������ʽ���䵽ǰ��

### ģ��ʹ��
1. templateģ�漯�ɻ������򻯴���
	* Django ʹ���ˡ�ģ��̳С��ĸ��ģ��̳�������ģ��ʹ���м������������ݣ�
	* ÿһ��ģ��ֻ��Ҫ���������صĲ��ּ��� 
	* �൱�������������ļ̳У����õĶ������ã��Լ��Ķ����Լ���
2. ���糣������ַ���֣�������ܣ��ܱ߶�����ͬ���䣬���ǰѹ�������ĵط��������Ϊ����ģ�棬������ҳ��̳�ģ��ֱ�����ù������֣�ͬʱ����Ҫ�ı�Ĳ��ֽ�����д�������������������������ƺ����� ʹ�������̶ȵĸ��ã�����ʹ��������ݸ��Ӽ򵥡�
3. ʵ�ʲ���
	* �û�����ģ��
~~~
		�û�����http��//192.138.0.120/hhhhh/list ����һ���û��б��Ա����ʽ����
~~~
4. ������� 
* ��·�ɲ���Ҫ�� ����Ӧ��·�� 
~~~
# cat hello/urls.py 
from django.urls import path,re_path
from . import views

app_name = 'hello'
urlpatterns = [
    path('list/',views.list,name='list'),
~~~
* ����views����
~~~
# cat hello/views.py 
from django.shortcuts import render
#����httpģ�棬ǰ����ʾ��ʽ
from django.http import HttpResponse,QueryDict
from django.shortcuts import render


def list(request):
    ##����б����ݣ�������ݿ�ȡ�������ݺ�������ֱ�������ݿ�ȡ
    users = [
        {'username': 'user1', 'name_cn': 'tom', 'age': 18},
        {'username': 'user2', 'name_cn': 'bob', 'age': 19},
        {'username': 'user3', 'name_cn': 'pop', 'age': 20},
    ]
    #�����һ��users.html�ļ����ڲ���
    return render(request, 'hello/users.html', {"users": users})
~~~
* �½�һ��users.html�ļ�������ʾ����
~~~
# cat templates/hello/users.html 
<html>
<head>
<title>�Զ�����άƽ̨</title>
</head>
<body>
<!-- ÿ��?ҳ?�涼�и���������ʽ����������䣬���Գ����������ı����������ɱ����� -->
<p style="background-color: #57ff2e;">����ģ�������ü���</p>
<p style="background-color:yellow;">�û��б�</p>
<!-- ?ҳ?�涼���������Ǳ仯����?һ�飬���ɱ��������� -->
<table border="1">
<thead>
<tr>
<th>�û���</th>
<th>����</th>
<th>����</th>
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
<!-- ÿ��ҳ�涼�и��ײ�����ʽ����������䣬���Գ������ -->
<p style="background-color:red;">��Ȩ���У�������</p>
</body>
</html>
~~~
* ����http://192.168.0.120:8000/hhhhh/list/  �õ���ͼ����

![�б����](G:\pythonʵս\pythonʵս��ϰ\�б����.jpg)

### ģ��̳�
   * ����url
~~~
# cat hello/urls.py 
from django.urls import path,re_path
from . import views

app_name = 'hello'
urlpatterns = [
    path('list/',views.list,name='list'),
~~~
* ��д��Ӧ��view����������û�����

~~~
# cat hello/views.py 
from django.shortcuts import render
#����httpģ�棬ǰ����ʾ��ʽ
from django.http import HttpResponse,QueryDict
from django.shortcuts import render


def list(request):
    ##����б����ݣ�������ݿ�ȡ�������ݺ�������ֱ�������ݿ�ȡ
    users = [
        {'username': 'user1', 'name_cn': 'tom', 'age': 18},
        {'username': 'user2', 'name_cn': 'bob', 'age': 19},
        {'username': 'user3', 'name_cn': 'pop', 'age': 20},
    ]
    #�����һ��list.html�ļ����ڲ���
    return render(request, 'hello/list.html', {"users": users})
~~~
* ��дtemplate�ļ� 
   * ����ĸ�棬ĸ�������ǹ��ò��� html�ļ� 
   * `������ {% block title %������ʼ������� titleΪ������ ��{% endblock %}` �������������`
   * `{% block ������ %} ���� {% endblock %}`
~~~
# cat templates/base.html 
<html>
<head>
<title>�Զ�����άƽ̨</title>
</head>
<body>
<!-- ÿ��ҳ�涼�и���������ʽ��������䣬���Գ����������ı����������ɱ��� -->
<p style="background-color:yellow;">
{% block title %} �û��б� {% endblock %}
</p>
<!-- ҳ������������Ǳ仯����һ�飬���ɱ������� -->
{% block content %}
{% endblock %}
<!-- ÿ��ҳ�涼�и��ײ�����ʽ��������䣬���Գ������ -->
<p style="background-color:red;">��Ȩ���У�������</p>
</body>
</html>

~~~
   * �̳�ĸ�� ��ҳ��̳�
~~~
# cat templates/hello/list.html 
{% extends "base.html" %}

~~~
   * ���̳�ʱ ���Ƿ���web �鿴���ͼ 
	 ![���̳�ĸ��](G:\pythonʵս\pythonʵս��ϰ\png\���̳�ĸ��.jpg)
  *  ��дĸ��仯���� 
~~~
# cat templates/hello/list.html 
{% extends "base.html" %}

{% block title %} �û����б� {% endblock %}

{% block content %}
<table border="1">
<thead>
    <tr>
        <th>�û���</th>
        <th>����</th>
        <th>����</th>
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



















