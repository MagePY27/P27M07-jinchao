from django.urls import path,re_path
from day4 import views

app_name = 'day4'
urlpatterns = [
    #查看筛选与添加
    path('index/', views.UserList.as_view(), name='index'),
    #修改
    re_path('daymod/(?P<pk>[0-9]+)?/', views.UserMod.as_view(), name='daymod'),
    #删除
    re_path('daydel/(?P<pk>[0-9]+)?/', views.UserDel.as_view(), name='userdel'),
]
