from django.contrib import messages
from django.http.request import QueryDict
import logging
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import reverse
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView ,DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from users.form import UserForm
from django.contrib.auth.models import Group, Permission
from contacts.models import Contacts

class CustomerListView(LoginRequiredMixin, PermissionRequiredMixin,View):
    """
    展示联系人，根据type筛选
    """
    permission_required = 'contacts.view_contacts'
    def get(self, request, pk):
        contactss = Contacts.objects.filter(type=pk)
        context = {'contactss': contactss}
        return render(request, "contacts/customer_list.html", context=context)

class ContactsAddView(LoginRequiredMixin, PermissionRequiredMixin,SuccessMessageMixin, CreateView):
    """
    添加联系人
    """
    template_name = "contacts/customer_form.html"
    permission_required = 'contacts.add_contacts'
    model = Contacts
    fields = ('name', 'sex', 'occupation', 'company', 'project', 'phone', 'type')
    success_message = '添加 %(name)s 联系人成功'
    def get_success_url(self):
        return reverse('contacts:contactsadd')

class ContactsupDataView(LoginRequiredMixin, PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    """
        编辑联系人
        """
    template_name = "contacts/customer_form.html"
    model = Contacts
    fields = ('name', 'sex', 'occupation', 'company', 'project', 'phone', 'type')
    permission_required = 'contacts.change_contacts'
    success_message = '更新 %(name)s 联系人成功'

    def get_success_url(self):
        return reverse('contacts:contactsupdata', kwargs={'pk': self.object.pk})


class ContactsDelView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'contacts.delete_contacts'

    def post(self, request):
        pk = request.POST.get('id')
        print(pk)
        try:
            contacts = Contacts.objects.filter(pk=pk)
            contacts.delete()
            msg = {"code": 0, 'result': "删除联系人成功"}
        except:
            logging.error("error is userdel")
            msg = {"code": 1, 'result': "删除联系人失败,请联系维护人员"}
        return JsonResponse(msg)