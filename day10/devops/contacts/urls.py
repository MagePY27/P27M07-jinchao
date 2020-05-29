from django.urls import path, re_path
from contacts.views import  *

app_name = 'contacts'

urlpatterns = [
    # 标签类型
    path('contactsadd/', ContactsAddView.as_view(), name='contactsadd'),
    re_path('customer/(?P<pk>[0-9]+)?/', CustomerListView.as_view(), name='customer'),
    re_path('contactsupdata/(?P<pk>[0-9]+)?/', ContactsupDataView.as_view(), name='contactsupdata'),
    re_path('contactsdel/', ContactsDelView.as_view(), name='contactsdel'),
]



