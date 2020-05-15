from django.urls import path, re_path
from users.views import *
from users.group import *
from users.userpermission import *

app_name = 'users'
urlpatterns = [
    # 用户管理
    path('', IndexView.as_view(), name='index'),
    path('userlist/', UserList.as_view(), name='userlist'),
    path('usersadd/', UserAdd.as_view(), name='usersadd'),
    re_path('usersdel/', UserDel.as_view(), name='usersdel'),
    re_path('usersmod/(?P<pk>[0-9]+)?/', UserMod.as_view(), name='usersmod'),


    # 权限管理
    path('userpermission/', UserPermission.as_view(), name='userpermission'),
    re_path('userpermission_updata/(?P<pk>[0-9]+)?/', UserPermissionUpdata.as_view(), name='userpermission_updata'),


    # 角色、用户组管理
    path('group_list/', GroupListView.as_view(), name='group_list'),
    path('group_add/', GroupAddView.as_view(), name='group_add'),
    re_path('group_update/(?P<pk>[0-9]+)?/',  GroupUpdateView.as_view(), name='group_update'),
    # 用户组添加用户
    re_path('group_add_user/(?P<pk>[0-9]+)?/', AddUserToGroupView.as_view(), name='group_add_user'),


    path('test/', Test.as_view(), name='tset'),

]