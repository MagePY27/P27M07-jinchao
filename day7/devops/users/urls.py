from django.urls import path, re_path
from users.views import *
from users.userpermission import *

app_name = 'users'
urlpatterns = [
    # 用户管理
    path('', IndexView.as_view(), name='index'),
    path('userlist/', UserList.as_view(), name='userlist'),
    path('usersadd/', UserAdd.as_view(), name='usersadd'),
    re_path('usersmod/(?P<pk>[0-9]+)?/', UserMod.as_view(), name='usersmod'),

    # 权限管理
    path('userpermission/', UserPermission.as_view(), name='userpermission'),
    re_path('userpermission_updata/(?P<pk>[0-9]+)?/', UserPermissionUpdata.as_view(), name='userpermission_updata'),



    path('test/', Test.as_view(), name='tset'),

]