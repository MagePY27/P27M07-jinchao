from django.urls import path,re_path
from hello import views2

app_name = 'hello'
urlpatterns = [
    #四种函数对应增删改查
    path('userlist/', views2.UserList.as_view(), name='UserList'),
    path('useradd/', views2.UserAdd.as_view(), name='UserAdd'),
    re_path('usermod/(?P<pk>[0-9]+)?/', views2.UserMod.as_view(), name='UserMod'),
    re_path('userdel/(?P<pk>[0-9]+)?/', views2.UserDel.as_view(), name='UserDel'),
]

