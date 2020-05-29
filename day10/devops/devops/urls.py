from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('cmdb/', include('cmdb.urls', namespace='cmdb')),
    path('contacts/', include('contacts.urls', namespace='contacts')),
]
