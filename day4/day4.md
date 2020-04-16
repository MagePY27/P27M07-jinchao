# day4 

### ����Ӧ��
~~~
# python manage.py startapp day4
# touch day4/urls.py
# tree day4/
day4/
������ admin.py
������ apps.py
������ __init__.py
������ migrations
��?? ������ __init__.py
������ models.py
������ tests.py
������ urls.py
������ views.py

1 directory, 8 files
~~~
### ע��app
~~~
# cat day4/apps.py 
from django.apps import AppConfig

class Day4Config(AppConfig):
    name = 'day4'
    
# cat devops/settings.py |grep INSTALLED_APPS -A 9
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello.apps.HelloConfig',
    'books.apps.BooksConfig',
    'day4.apps.Day4Config'
~~~
### ����ȫ��urls
~~~
# cat devops/urls.py  |grep django.contrib  -A 10
urlpatterns = [
#����batman��urlת��hello��urls�Լ���
    path('hello/',include('hello.urls'),name="hello"),
    path('day4/',include('day4.urls'),name="day4"),
]
~~~

### ��ģ
~~~
# cat day4/models.py 
from django.db import models

class Day4(models.Model):
    SEX = (
        (0,'��'),
        (1,'Ů'),
    )
    SKILL = (
        (0,'Python'),
        (1,'Java'),
        (2,'PHP'),
        (3,'C#'),
    )
    name = models.CharField(max_length = 20,help_text='�û���')
    password = models.CharField(max_length=32,help_text="����")
    tel = models.CharField(max_length=11,help_text="�绰")
    email = models.CharField(max_length=35,help_text="����")
    sex = models.IntegerField(choices = SEX,null=True,blank=True)
    skill = models.IntegerField(choices=SKILL, null=True, blank=True)
    def __str__(self):
        return self.name
- ����Ǩ�ƽű�     
#  python manage.py makemigrations day4
Migrations for 'day4':
  day4/migrations/0001_initial.py
    - Create model Day4
- �鿴�����ļ�
#  cat day4/migrations/0001_initial.py 
# Generated by Django 2.2 on 2020-04-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='�û���', max_length=20)),
                ('password', models.CharField(help_text='����', max_length=32)),
                ('tel', models.CharField(help_text='�绰', max_length=11)),
                ('email', models.CharField(help_text='����', max_length=35)),
                ('sex', models.IntegerField(blank=True, choices=[(0, '��'), (1, 'Ů')], null=True)),
                ('skill', models.IntegerField(blank=True, choices=[(0, 'Python'), (1, 'Java'), (2, 'PHP'), (3, 'C#')], null=True)),
            ],
        ),
    ]
    
-ִ����䴴�����ݿ�
# python manage.py migrate day4
~~~

### ���app url
~~~
# cat day4/urls.py 
from django.urls import path,re_path
from day4 import views

app_name = 'day4'
urlpatterns = [
    #�鿴ɸѡ������
    path('index/', views.UserList.as_view(), name='index'),
    #�޸�
    re_path('daymod/(?P<pk>[0-9]+)?/', views.UserMod.as_view(), name='daymod'),
    #ɾ��
    re_path('daydel/(?P<pk>[0-9]+)?/', views.UserDel.as_view(), name='userdel'),
]
~~~
### ��ƶ�Ӧviews
~~~
# cat day4/views.py 
from django.shortcuts import render
from django.shortcuts import reverse
from day4.models import Day4
from django.views.generic import ListView,DeleteView,UpdateView,TemplateView
from django.contrib.messages.views import SuccessMessageMixin
import os
from day4.form import UserForm

#�б�ɸѡ������
class UserList(SuccessMessageMixin,ListView):
    template_name = 'day4/index.html'
    model = Day4
    context_object_name = 'users'
    success_message = "%(name)s ���ӳɹ�������"
    #ɸѡ
    def get_queryset(self):
        queryset = super(UserList,self).get_queryset()
        self.keyword = self.request.GET.get("keyword","")
        if self.keyword :
            print(queryset)
            queryset = queryset.filter(name__icontains=self.keyword)
            print(queryset)
        return queryset
    ##�����û�ҳ����ת
    def get_template_names(self):
        names = super().get_template_names()
        if 'add' in self.request.GET:
            names = ['day4/dayadd.html']
        return names
    ###�����û�
    def post(self, request):
        user_input_obj = UserForm(request.POST)
        print(user_input_obj)
        if user_input_obj.is_valid():
            #��֤�ɹ����ļ��ϴ�
            file = request.FILES.get('file', None)
            if file:
                f = open(os.path.join('upload', file.name), 'wb')
                for line in file.chunks():
                    f.write(line)
                f.close()
        else:
            #��֤ʧ�ܷ�����֤��Ϣ
            form = user_input_obj.errors ##��ȡ������Ϣ
            print(form)
            return render(request, 'day4/dayadd.html', {'form': form})
        self.html = 'day4/index.html'
        data = request.POST.dict()
        if '_save' in data:
            data.pop('_save')
            Day4.objects.create(**data)
            self.html = 'day4/dayadd.html'
        users = Day4.objects.all()
        return render(request, self.html,{"users": users})
#�б�ɾ��
class UserDel(DeleteView):
    model = Day4
    template_name = 'day4/daydel.html'
    def get_success_url(self):
        return reverse('day4:index')

#�б��޸�
class UserMod(SuccessMessageMixin,UpdateView):
    success_message = "%(name)s �޸ĳɹ�������"
    template_name = 'day4/daymod.html'
    model = Day4
    context_object_name = 'user'
    fields = ('name','password','sex','tel','email','skill')
    def get_success_url(self):
        if 'return' in self.request.POST:
            return reverse('day4:index')
~~~


### ��Ӧhtml
- index.html
~~~
# cat templates/day4/index.html 
{% extends "base.html" %}

{% block title %} �û���Ϣ {% endblock %}

{% block content %}

<form method="get"  action="/day4/index/" >
    �������û�����
    <input type="text" name="keyword" value="{{object.id}}">
    <button type="submit" value="Submit" >��ѯ </button>
    <input type="submit" name="add" value="����" >
</form>
<table border="2">
<thead>
    <tr>
        <th>ID</th>
        <th>�û���</th>
        <th>����</th>
        <th>�Ա�</th>
        <th>�绰</th>
        <th>����</th>
        <th>����</th>
        <th>�༭</th>
    </tr>
</thead>
<tbody>
    {% for user in users %}
    <tr>
        <td>{{ user.id}} </td>
        <td>{{ user.name }}</td>
        <td>{{ user.password }}</td>
        <td>
            {% if user.sex == 0 %} �� {% elif user.sex == 1%} Ů {% else %} δ���� {%endif%}
        </td>
        <td>{{ user.tel}} </td>
        <td>{{ user.email}} </td>
        <td>
        {% if user.skill == 0 %} Python {% elif user.skill == 1%} Java {% elif user.skill == 2 %}PHP {% elif user.skill == 3%} C# {% else %} δ���� {%endif%}
        </td>

        <td>
            <button><a href="/day4/daymod/{{user.id}}">�޸�</a></button>
            <button><a href="/day4/daydel/{{user.id}}" >ɾ��</a></button>

        </td>
    </tr>
    {% endfor %}


</tbody>
</table>
~~~
- �����û�ҳ��
~~~
# cat templates/day4/dayadd.html 
{% extends "base.html" %}

{% block title %} �����û� {% endblock %}

{% block content %}

{% if messages %}
<ul>
    {% for message in messages %}
    <li {% if message.tags %} class="{{ message.tags }}"{% endif %}>{{message}}</li>
    {% endfor %}
</ul>
{% endif %}

<form method="post"  action="/day4/index/" enctype="multipart/form-data" >
    ����:
    <input type="text" name="name" >
    <br>
    {% if form.name %}
    <p style="color: red">{{form.name}}</p>
    {% endif%}
    <br>
    ����:
    <input type="password" name="password">
    <br>
    {% if form.password %}
    <p style="color: red">{{ form.password}}</p>
    {% endif%}
    <br>
    �绰:
    <input type="text" name="tel">
    {% if form.tel %}
    <p style="color: red">{{ form.tel}}</p>
    {% endif%}
    <br>
    <br>
    ����:
    <input type="text" name="email">
    {% if form.email %}
    <p style="color: red">{{ form.email}}</p>
    {% endif%}
    <br>
    <br>
    �Ա�:
    <input type="radio" name="sex" value="0" checked>��
    <input type="radio" name="sex" value="1">Ů
    <br>
    <br>
    ����:
    <select name="skill">
        <option value="0" selected>Python</option>
        <option value="1" >Java</option>
        <option value="2" >PHP</option>
        <option value="3">C#</option>
    </select>
    <br>
    <br>
     ���Ӹ���:
    <input type="file" name="file" >
    {% if form.file %}
    <p style="color: red">{{ form.file}}</p>
    {% endif%}
    <br>
    <input type="submit" value="����" name="_save">
    <button> <a href="/day4/index/" >����</a> </button>
</form>



{% endblock %}
~~~

- �޸�ҳ��
~~~
# cat templates/day4/daymod.html 
{% extends "base.html" %}

{% block title %} �޸��û���Ϣ {% endblock %}

{% block content %}

{% if messages %}
<ul>
    {% for message in messages %}
    <li {% if message.tags %} class="{{ message.tags }}"{% endif %}>{{message}}</li>
    {% endfor %}
</ul>
{% endif %}

{% if form %}
<ul>
    {{form.errors}}
</ul>
{% endif %}

<form method="post"><br>
ID��<br>
<input type="text" name='id' value={{user.id}} readonly="readonly">
    <br>
�û�����<br>
<input type="text" name = 'name' value={{user.name}} >
    {% if form.name %}
    <p style="color: red">{{ form.name.errors}}</p>
    {% endif%}
����:<br>
<input type="text" name="password" value={{user.password}}>
    {% if form.password %}
    <p style="color: red">{{ form.password.errors}}</p>
    {% endif%}
�绰:<br>
<input type="text" name="tel" value={{user.tel}}>
    {% if form.tel %}
    <p style="color: red">{{ form.tel.errors}}</p>
    {% endif%}
����:<br>
<input type="text" name="email" value={{user.email}}>
    {% if form.email %}
    <p style="color: red">{{ form.email.errors}}</p>
    {% endif%}
�Ա�:<br>
    <input type="radio" name="sex" value="0" checked>��
    <input type="radio" name="sex" value="1">Ů
    <br>
����:<br>
    <input type="radio" name="skill" value="0" checked>Python
    <input type="radio" name="skill" value="1">PHP
    <input type="radio" name="skill" value="2">Java
    <input type="radio" name="skill" value="3">C#
<br><br>
    <input type="submit" value="�޸�" >
    <input type="submit" value="����" name="return" >
</form>
{% endblock %}
~~~

- ɾ��ҳ��
- 
~~~
# cat templates/day4/daydel.html 
{% extends "base.html" %}

{% block title %} ȷ��ɾ���û� {% endblock %}

{% block content %}


<table border="1" >
<thead>
    <tr>
        <th>ID</th>
        <th>�û���</th>
        <th>����</th>
        <th>�Ա�</th>
    </tr>
</thead>
<tbody>
<tr>
    <td>{{ object.id}} </td>
    <td>{{ object.name }}</td>
    <td>{{ object.password }}</td>
    <td>
        {% if object.sex == 0 %} �� {% elif object.sex == 1%} Ů {% else %} δ���� {%endif%}
    </td>
</tr>
</tbody>
</table>
<form  method="post" >
    <button type="submit">ȷ�� </button>
    <button> <a href="/day4/index/" >����</a> </button>
</form>

{% endblock %}

~~~
- ��������ļ�
- 
~~~
# cat day4/form.py 
from django import forms
from day4.models import Day4

class UserForm(forms.Form):
    #���������Сֵ��Ĭ�ϲ�����Ϊ��
    name = forms.CharField(max_length=10)
    password = forms.CharField(min_length=6,required=True)
    tel = forms.CharField(max_length=11,min_length=11,required=True)
    email = forms.CharField(max_length=32,required=True)
    file = forms.FileField(required=False)

    def clean_info(self):
        info = self.changed_data['info']
        print(info.split())
        num_info = len(info.split())
        if num_info <4 :
            raise forms.ValidationError('Info not enough words!')
        return info

~~~

### ������ʾ
![ɸѡ](G:\pythonʵս\pythonʵս\day4\ɸѡ.png)
![�޸�](G:\pythonʵս\pythonʵս\day4\�޸�.png)
![����](G:\pythonʵս\pythonʵս\day4\����.png)












