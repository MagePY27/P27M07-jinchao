"""devops URL Configuration

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
from django.urls import path,re_path
#从hello（我们之前创建了的目录）中调用views.py文件，这个里面会写对应的函数index
#from hello import views
#导入include url转向
from django.urls import path,include
urlpatterns = [
#访问batman将url转给hello的urls自己理
    path('hello/',include('hello.urls')),
    path('admin/', admin.site.urls),
#参考上面系统自建的放完admin就进入用户界面，我们添加一个访问hello就进入我们给定的函数
#    path('hello/',views.index),

]

