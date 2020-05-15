from django.contrib import messages
import logging
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Group, Permission

from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.views.generic.base import View, TemplateView
from pure_pagination.mixins import PaginationMixin
from django.contrib.auth import get_user_model

User = get_user_model()

class GroupListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    组列表
    """
    template_name = 'users/group_list.html'
    model = Group
    context_object_name = "groups"
    permission_required = 'auth.view_group'
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



class GroupAddView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """
    添加组
    """
    template_name = 'users/group_add.html'
    model = Group
    fields = ('name', 'permissions')
    success_message = '%(name)s 组添加成功！'
    permission_required = 'auth.add_group'


    def get_success_url(self):
        return reverse('users:group_add')

    # 增加前端权限列表
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        permissions = Permission.objects.exclude(Q(content_type__model='session') |
                                                 Q(content_type__model='contenttype') |
                                                 Q(content_type__model='logentry') |
                                                 Q(codename='add_permission') |
                                                 Q(codename='delete_permission')|
                                                 Q(codename='change_permission')
                                                 ).values('id', 'name',
                                                          'content_type__app_label',
                                                          'codename')
        context['permissions'] = permissions
        return context


class GroupUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    更新组
    """
    template_name = 'users/group_update.html'
    model = Group
    fields = ('name', 'permissions')
    success_message = '%(name)s 组更新成功！'
    permission_required = 'auth.change_group'

    def get_success_url(self):
        return reverse('users:group_update', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        permissions = Permission.objects.exclude(Q(content_type__model='session') |
                                                 Q(content_type__model='contenttype') |
                                                 Q(content_type__model='logentry') |
                                                 Q(codename='add_permission') |
                                                 Q(codename='delete_permission')|
                                                 Q(codename='change_permission')
                                                 ).values('id', 'name',
                                                          'content_type__app_label',
                                                          'codename')
        context['permissions'] = permissions
        return context


class AddUserToGroupView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    批量将用户添加到组
    """
    permission_required = 'auth.change_group'

    def get(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        users = User.objects.exclude(username__icontains="admin")
        context = {'group': group, 'users': users}
        return render(request, 'users/group_add_user.html', context=context)

    def post(self, request, pk):
        uids = request.POST.getlist('users')
        group = get_object_or_404(Group, pk=pk)
        if uids:
            users = User.objects.filter(id__in=uids)
            group.user_set.set(users)
        else:
            group.user_set.clear()
        messages.success(request, '{}组添加用户或移除用户成功！'.format(group))
        if '_addanother' in request.POST:
            return HttpResponseRedirect(reverse('users:group_add_user', kwargs={'pk': pk}))
        return HttpResponseRedirect(reverse('users:group_list'))











