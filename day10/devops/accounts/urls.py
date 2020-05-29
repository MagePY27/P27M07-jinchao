from django.urls import path, re_path
from accounts import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path("logout", views.LogoutView.as_view(), name='logout'),
    re_path("passwordmod/(?P<pk>[0-9]+)?/", views.PasswordMod.as_view(), name='passwordmod'),

]