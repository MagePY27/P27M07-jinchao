# WEB��ܵ�����߼�MVC&&MTV
### һ���û�������ַ�س��󶼷�����ʲô��
~~~
   ���û��Ƕȷ���Django��ܣ���վ������Ҫ��Щ����������MVC(MTV)�������ô���ģ�
~~~

   * �û�������ַ��������<-->·��/url��·�꣺�����û��������ַ����������˭������Django��ͨ��urls.py�ļ���ά��·��--> �������Ķ�Ӧ��ϵ��ԭ������ͨ����·�ɽ����������������ݣ���·��Ҳ���Խ�������·�����������վ���·�ɶ���ת��������view��
   * �û����������˭��������ô���� <-->view(������/������)���û��������ַ���ջᱻ·�ɣ�urls��ָ���Ӧ�Ŀ�����������Django��ͨ��viwes.py�ļ����崦���߼��������ݽ��д���
   * �û���Ҫ�����ݴ�������<-->model(ģ��)���ṹ���Ĵ洢�û���Ҫ���ݣ����������������ݴ洢��model���û���Ҫ����ʱ����������������ӹ����ظ��û���Django�е�model.py �ж�����ģ�ͣ�Ҳ�������ݱ�ṹ��*��˵���Ǵ���ȡ���ݵĵط����û�ȡ�����������ã����������Ҳ������ȡ*��
   * �û���ο����Լ���Ҫ�����ݣ�<-->template��ģ�棩��ģ�渺��views����������õ����ݣ�һ�㱻ת����list��dict��json����Ⱦ���û��ܿ������׵ĸ�ʽ������html��չ�ִ���õ����ݣ�*��˵���ǽ�������õ����ݽ���ǰ�˽�����ʾ����������г�ֵ�ǰ�˼����������ķǳ�Ư�������û�еĻ�Ҳ��������ģ������������������ϰ�һЩ���˺ÿ���ģ�滻���Լ������ݣ��൱�ڰ����ݴ����·���������Ϊ������ѡ�ÿ����·�*��
	* ����ͼ����
	![����ͼ](G:\pythonʵս\pythonʵս��ϰ\����ͼ.png)
	 
### ������ʶDjango�ṹ������Django���
~~~
����Django�ṹ������ǰ���
~~~
   1. ��������Ŀ¼��֮ǰ���Ǵ�����devops����Ŀ¼��
~~~
# tree devops/
devops/
������ __init__.py					 	###��ʼ���ļ�����������һ����
������ __pycache__					 	
��   ������ __init__.cpython-36.pyc		
��   ������ settings.cpython-36.pyc		
��   ������ urls.cpython-36.pyc			
��   ������ wsgi.cpython-36.pyc			
������ settings.py						###���������������ļ� 
������ urls.py							###������·�ɣ�����·��·��
������ wsgi.py							###����web��������ڣ�nginx/apache��
~~~
   2. ����app��Ӧ�ã�Ŀ¼������֮ǰ������helloӦ�ã�
~~~
# tree hello/
hello/
������ admin.py							##��̨�����ļ�
������ apps.py							##app�����ļ��������������ļ���������������ݣ�
������ __init__.py						##��ʼ���ļ���Ĭ��Ϊ��
������ migrations						##����Ǩ���ļ�
��   ������ __init__.py
��   ������ __pycache__
��       ������ __init__.cpython-36.pyc
������ models.py						##ģ���ļ�
������ __pycache__						##������������һ�κ󣬺�������ģ�鲻�ı�����¼ӿ��������ļ�	
��   ������ admin.cpython-36.pyc
��   ������ apps.cpython-36.pyc
��   ������ __init__.cpython-36.pyc
��   ������ models.cpython-36.pyc
��   ������ urls.cpython-36.pyc
��   ������ views.cpython-36.pyc
������ tests.py
������ urls.py							##����·�ɣ�Ĭ��û�У��������
������ views.py							##�߼�����������
~~~
   3. ��ȫ�������ļ���ע���´�����app
	  *  �����￴���app��Ϣ
~~~
# cat hello/apps.py 
from django.apps import AppConfig


class HelloConfig(AppConfig):
    name = 'hello'
~~~ 	
4. * ��ȫ�������ļ���ע�� 
~~~
# cat devops/settings.py |grep INSTALLED_APPS  -A 9
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello.apps.HelloConfig'   				###�������ö�Ӧ��Ӧ��apps.py����Ϣ����������������̾Ϳ����ҵ�Ӧ����
]
~~~
5.   * ��д��url·��ʹ�û��ܹ��ҵ���Ӧ������
~~~
# cat devops/urls.py
from django.contrib import admin
from django.urls import path,re_path
from hello import views						#��hello������֮ǰ�����˵�Ŀ¼���е���views.py�ļ�����������д��Ӧ�ĺ���index
from django.urls import path,include		#����include urlת��
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('hello/',views.index),				#���û�url��дhello��ֱ�ӵ��ö�Ӧ�ĺ�������
    path('hhhhh/',include('hello.urls'))	#����hhhhh��urlת��Ӧ��hello�Լ���urls����
]

~~~

6.   * ��дӦ���Լ���url·�� 
~~~
# cat hello/urls.py 
from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path('(?P<year>[0-9]{4})/(?<month>[0-9]{2})',views.index,name='index'),
#���ӵ���url��ת������url��ƴ������url����ǿͻ����ʵ�url����ͨ��url·�ɶ�Ӧ��������ͬ���߼�����
    path('cpu/',views.cpu,name='index'),
    path('free/',views.free,name='index'),
    path('ip/',views.ip,name='index'),
    path('ping/',views.ping,name='index'),

]
~~~
7.   * ����·���Ѿ�ָ���˴���������ô����������Ϊ��������д����߼�
~~~
# cat hello/views.py 
from django.shortcuts import render
from django.http import HttpResponse


###���û�����hello·�ɣ�ip:8000/hello)ʱ��������·��ֱ�ӵ���views��index���� 
def index(request):
    return HttpResponse("<p>hello world,hello,django</p>")
###���û�����hhhhh·�ɣ�ip:8000/hello/***��ʱ,������·��ת��Ӧ������·�ɣ�����·��ƴ��Ӧ������·�ɺ󷵻ض�Ӧ��ͬ�ĺ���
def cpu(request):
    return HttpResponse("<p>'mycpu is 88% </p>")
def ip(request):
    return HttpResponse("<p>'ip: 192.168.0.120 </p>")
def free(request):
    return HttpResponse("<p>'free is 50%</p>")
def ping(request):
    return HttpResponse("<p>'192.168.0.120��s ping OK'</p>")

~~~
8.   * ͨ��������� �Ϳ��Է���web�������õ����Ǽ򵥵�������
### ����MTV��ͼ��url&&view��
~~~
ͨ�������url��ƣ�������ͨ��ǰ�˵���˵����ӣ��ܽ�������ݱ��ֵ������ϣ���ô������Ҫ�����û���ͬ�������д��get/post�� 
~~~

   1.  request && response
~~~
	1. request ���� �û��������࣬��С��Է�������������
		- get����
			- ��������										 #1��
			- ������										
				-  ������      -- url						 #2��
				-  λ�ò���    -- url���					 #3��
				-  �ؼ��ֲ���  -- url��� 					 #4��
	    - post ������������¶��������������������� 	 #5��
~~~
  2. response ���� 2����3С���ȡ������
~~~
		* request.method  ���� �ж�����ķ�ʽ 
		* request.body ���� ��һ�ֻ�ȡ���ݵķ���
			* print(type(request.body)) # byte
			* print(QueryDict(request.body)) # QueryDict
			* print(QueryDict(request.body).dict) # dict
		* request.GET # ��2�ַ�ʽ��ȡGET QueryDict 
 			* request.GET.get('name','devops') 
		* request.POST # ��2�ֻ�ȡpost���ݷ�ʽ <QueryDict: {'year':['2019']
			* request.POST.getlist��'id'��
		*  kwargs.get('year', 2020) # �����ֻ�ȡGET ֻ��?�ؼ������������
   3.  ���������Ķ� ����get
		* �û������������url
			* ֮ǰ�Ѿ����õļ򵥵�url��Ʒ���http://192.168.0.120:8000/hhhhh/ �õ�index�������ؽ��

~~~
3. �ο�֮ǰappӦ�� cat hello/urls.py 
~~~
from django.urls import path,re_path
from . import views

urlpatterns = [
    #re_path('(?P<year>[0-9]{4})/(?<month>[0-9]{2})',views.index,name='index'),
#���ӵ���url��ת������url��ƴ������url����ǿͻ����ʵ�url
    path('',views.index,name='index'),			###������Ϊ�յ�ʱ�����index����
    path('cpu/',views.cpu,name='index'),
    path('free/',views.free,name='index'),
    path('ip/',views.ip,name='index'),
    path('ping/',views.ping,name='index'),

]


# cat hello/views.py 
from django.shortcuts import render
#����httpģ�棬ǰ����ʾ��ʽ
from django.http import HttpResponse


#����index��������·��ָ��
def index(request):
    return HttpResponse("<p> hello Djang </p> ")

def cpu(request):
    return HttpResponse("<p>'mycpu is 88% </p>")
def ip(request):
    return HttpResponse("<p>'ip: 192.168.0.120 </p>")
def free(request):
    return HttpResponse("<p>'free is 50%</p>")
def ping(request):
    return HttpResponse("<p>'192.168.0.120��s ping OK'</p>")

~~~              
4. �������Ķ� ���� get
   1. �û������������url
~~~
		�����ֳ���
			1����ͨ����
				http://192.168.0.120:8000/hhhhh/?year=2019&month=06
			2��λ�ò���
				http��// 192.168.0.120://hhhhh/2019/06
			3���ؼ��ִ���
			    http��// 192.168.0.120://hhhhh/2019/06
~~~	
5. ����views.py�ļ�����Ӧ������ͬ��url����
~~~
###����views.py�ļ� 
# cat hello/views.py 
from django.shortcuts import render
#����httpģ�棬ǰ����ʾ��ʽ
from django.http import HttpResponse

#��ͨ��������
def index(request):
    #2020 88  Ϊȱʡֵ �������� ������û�д��λᱨ��
    year = request.GET.get('year','2020')
    month = request.GET.get('month','88')
    return HttpResponse("year is %s,month is %s" % (year,month) )
#λ�ô���
def Location(request,year,month):
    return HttpResponse('year is {},month is {} '.format(year,month) )
#�ؼ��ִ���
def keywords(request,**kwargs):
    year = kwargs.get('year',2022)
    month = kwargs.get('month',9)
    return HttpResponse('year is {},month is {} '.format(year,month) )
# Create your views here.
			
~~~
6. ���ö�Ӧurl�ļ�
   1. ��ͨ���ղ���
~~~
###��ͨ����
# cat hello/urls.py 
from django.urls import path,re_path
from . import views

urlpatterns = [
#���ӵ���url��ת������url��ƴ������url����ǿͻ����ʵ�url
#��ͨurl ���޲���url����    
    path('',views.index,name='index'),
#λ��ƥ��
#    re_path("([0-9]{4})/([0-9]{2})",views.Location,name='Location'),

]

###���ʶ�Ӧurl �������������ʱĬ��Ϊȱʡֵ
http://192.168.0.120:8000/hhhhh/
year is 2020,month is 88
�����������Ҫ��Ӧ�������ֻ����һ����������һ������ʹ��ȱʡֵ
http://192.168.0.120:8000/hhhhh/?year=2222&month=11
year is 2222,month is 11
~~~
   2. λ�ô��� 
~~~
* cat hello/urls.py 
from django.urls import path,re_path
from . import views

urlpatterns = [
#���ӵ���url��ת������url��ƴ������url����ǿͻ����ʵ�url
#��ͨurl ���޲���url����    
#    path('',views.index,name='index'),
#λ��ƥ��
    re_path("([0-9]{4})/([0-9]{2})",views.Location,name='Location'),
#�ؼ���ƥ��
#re_path("(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/",views.keywords,name='keywords'),
]


http://192.168.0.120:8000/hhhhh/1444/44
year is 1444,month is 44
~~~
   3. �ؼ��ִ��� ��urlʱ�͹涨�˹ؼ��֣������˲�����
~~~
# cat hello/urls.py 
from django.urls import path,re_path
from . import views

urlpatterns = [
#���ӵ���url��ת������url��ƴ������url����ǿͻ����ʵ�url
#��ͨurl ���޲���url����    
#    path('',views.index,name='index'),
#λ��ƥ��
#    re_path("([0-9]{4})/([0-9]{2})",views.Location,name='Location'),
#�ؼ���ƥ��
    re_path("(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/",views.keywords,name='keywords'),
]

http://192.168.0.120:8000/hhhhh/5555/11/
year is 5555,month is 11 

~~~	
7. ��������д����post ������get���󣬲����������Ƕ�ȡ���Ĭ�ϵ�ȱʡֵ���������������൱�ڶ�ȡ�ֵ��valueֵ��
	* ���ýӴ�url
~~~
# vim hello/urls.py 

from django.urls import path,re_path
from . import views

urlpatterns = [
    path('hello/',views.index,name='index'),
~~~
   * ���ö�Ӧ�Ĵ�����
~~~
# cat hello/views.py 
from django.shortcuts import render
#����httpģ�棬ǰ����ʾ��ʽ
from django.http import HttpResponse,QueryDict

#����������գ�Ĭ��Ϊget����ͨ��method�ж�POST����
###���ǽӵ��û���������request��Ϣ�кܶ࣬ͨ����ͬ�Ĳ����鿴�����Ϣ
def index(request):
    print(request.scheme)	###http ������
    print(request.method)	###���Ͳ鿴�û�����������ʲô���� �ֱ�����ش������� GET��POST��delete put
    print(request.headers)	###���ǳ�˵��headͷ����Ϣ
    print(request.path)		###path ·�� url��Ϣ
    print(request.META)		###���ǳ�˵��Header��Ϣ����������˺ܶ���Ϣ���û���ַ ��������ַ����Ϣ�����Կ����ĸ��û������� 
    print(request.GET)		###QueryDict���ͣ���˵����python�����ǵ�get�����װ���ֵ����ͣ��Է���������ȡ���� 
    data = request.GET
    year = data.get("year","8888")
    month = data.get("month","88")
    if request.method == "POST":  ###ͨ��method �ж���get����post����
#        print(request.method)	  #��ӡ����
#        print(request.body)	  #body��Ϣ
#        print(QueryDict(request.body).dict()) ##��һ��������
#        print(request.POST)	
        data = request.POST			#python�Ѿ������ݷ�װ����POST ����ֱ����POST��getȡ�������
        year = data.get("year","6666")
        month = data.get("month", "66")
    return HttpResponse("year is %s,month is %s" % (year,month) )
~~~
   * ͨ��web��������ȡget��������� ʹ��ȱʡֵ����Ա�post
~~~
	http://192.168.0.120:8000/hhhhh/hello/
  * ������Ϣ
	year is 8888,month is 88
~~~
   * ͨ��curlģ������
~~~
	#curl -X POST http://192.168.0.120:8000/hhhhh/hello/ -d 'year=2020&month=22'
	year is 2020,month is 22
	* ͨ��curl����ȱʡֵ
	#curl -X POST http://192.168.0.120:8000/hhhhh/hello/ -d ''
	year is 6666,month is 66
	* �������ǿ��Կ��� ������ȱʡֵʱ ���õķ�����Ϣ��ͬ һ��֤�������� get��post���� �Դ����Ǳ���Զ�get��post�������ֱ�Ĵ�����view���� 
~~~
   * ���curl post��������ǰ�ȫ��֤������ ���԰Ѱ�ȫ��֤�ر� ���̵�setting�ļ�����
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

###   �ܽ�
* �˽��û��Ĳ�ͬ�������� get����post
* Ĭ��request��get���� ͨ��request.method ���ж��Ƿ���post����
* QueryDict pythonΪ���������Ż����� ����ǰ���������Բ�ͨ Django��ǰ������ת��Ϊ�����Ƿ��㴦���dict����
* ��Ҫͨ�� request.GET.get ��request.HOST.get ����ȡ������� ������











		

		
