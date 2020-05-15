from django.urls import path,re_path
from Pj_information import views

app_name = 'Pj_information'
urlpatterns = [
    # 设置应用自身url 定义访问url时去哪取对应操作
    path('informationlist/', views.InformationList.as_view(), name='informationlist'),
    path('informationadd/', views.InformationAdd.as_view(), name='informationadd'),
    re_path('informationmod/(?P<pk>[0-9]+)?/', views.InforMod.as_view(), name='informationmod'),
]

