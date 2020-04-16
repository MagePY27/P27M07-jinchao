from django.urls import path,re_path
from hello import views3

app_name = 'hello'
urlpatterns = [
    #四种函数对应增删改查
    path('userlist/', views3.UserList.as_view(), name='userlist'),
    path('useradd/', views3.UserAdd.as_view(), name="useradd"),
    re_path('usermod/(?P<pk>[0-9]+)?/', views3.UserMod.as_view(), name='UserMod'),
    re_path('userdel/(?P<pk>[0-9]+)?/', views3.UserDel.as_view(), name='UserDel'),
]

