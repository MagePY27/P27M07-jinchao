from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView ,DetailView
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
import logging
from django.shortcuts import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

class UserPermission(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    permission_required = 'auth.view_permission'
    template_name = "users/users_permission.html"
    model = Permission
    context_object_name = "users"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(content_type__model__in=['logentry', 'session', 'contenttypr'])

        return queryset
    def post(self, request):
        pk = request.POST.get('id')
        try:
            user = self.model.objects.filter(pk=pk)
            user.delete()
            msg = {"code": 0, 'result': "删除用户组成功"}
        except:
            logging.error("error is userdel")
            msg = {"code": 1, 'result': "删除用户组失败,请联系维护人员"}
        return JsonResponse(msg)

class UserPermissionUpdata(LoginRequiredMixin,PermissionRequiredMixin, SuccessMessageMixin,UpdateView):
    permission_required = 'auth.change_permission'
    template_name = "users/users_permission_update.html"
    model = Permission
    success_message = '%(name)s 更新成功！'
    fields = ('name',)

    def get_success_url(self):
        return reverse('users:userpermission_updata', kwargs={'pk': self.kwargs['pk']})
