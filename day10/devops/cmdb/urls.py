from django.urls import path, re_path
from .views import  *

app_name = 'cmdb'

urlpatterns = [
    # 标签类型
    path('types/', TypeListView.as_view(), name='types'),
    path('types_add/', TypeAddView.as_view(), name='type-add'),
    re_path('types_edit/(?P<pk>[0-9]+)?/', TypeEditView.as_view(), name='type-edit'),
    re_path('types_delete/(?P<pk>[0-9]+)?/', TypeDeleteView.as_view(), name='type-delete'),

    # 标签
    path('tags/', TagListView.as_view(), name='tags'),
    path('tags_add/', TagAddView.as_view(), name='tag-add'),
    re_path('tags_edit/(?P<pk>[0-9]+)?/', TagEditView.as_view(), name='tag-edit'),
    re_path('tags_delete/(?P<pk>[0-9]+)?/', TagDeleteView.as_view(), name='tag-delete'),
    re_path('add_hosts/(?P<pk>[0-9]+)?/', Add_HostsView.as_view(), name='add-hosts'),

    # 资源管理
    path('hosts/', Hosts.as_view(), name='hosts'),
    path('overview/', Overview.as_view(), name='overview'),
    re_path('hosts_p/(?P<pk>[0-9]+)?/', Hosts_p.as_view(), name='hosts_p'),




]