from django.urls import path,re_path
from hello import views

app_name = 'hello'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name="index"),
    path('userlist/', views.UserList.as_view(), name="userlist"),
    re_path('usermod/(?P<pk>[0-9]+)?/', views.UserMod.as_view(), name='usermod'),
    re_path('userdel/(?P<pk>[0-9]+)?/', views.UserDel.as_view(), name='userdel'),


    #测试页面
    path('test/', views.HtmlTest.as_view(), name="test"),

]

