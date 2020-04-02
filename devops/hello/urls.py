from django.urls import path,re_path
from . import views

app_name = 'hello'
urlpatterns = [
#访问列表url
    path('list/',views.list,name='list'),
#删除数据时调用userdel函数
    re_path('userdel/([0-9]{1,3})',views.userdel,name='userdel'),
#修改时转到修改界面
    re_path('usermod/([0-9]{1,3})',views.usermod,name='usermod'),
#修改完成后，对数据库进行操作
    re_path('usermod/usermod_ok',views.usermod_ok,name='usermod_ok'),
#新增时转入新增界面
    path('usernew/', views.usernew, name='usernew'),
#新增数据完成后，对数据库进行操作
    re_path('usernew/usernew_ok', views.usernew_ok, name='usernew_ok'),
]

