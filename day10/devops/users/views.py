from django.contrib import messages
from django.http.request import QueryDict
import logging
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import reverse
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView ,DetailView
# from pure_pagination.mixins import PaginationMixin
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from users.form import UserForm
from django.contrib.auth.models import Group, Permission


# django自带认证模块
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required




User = get_user_model()
# 首页
class IndexView(LoginRequiredMixin, TemplateView):
    """
    首页
    """
    template_name = "index.html"
# 列表 删除与筛选 筛选用前端完成这里不实现
class UserList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'users.view_userprofile'
    template_name = "users/users_list.html"
    model = User
    context_object_name = "users"
    # 不显示admin
    def get_queryset(self):
        queryset = super(UserList, self).get_queryset().exclude(username__icontains="admin")
        return queryset
# 添加用户
class UserAdd(LoginRequiredMixin,PermissionRequiredMixin, TemplateView):
    permission_required = "users.add_userprofile"
    template_name = "users/users_add.html"
    def post(self, request):
        msg = {}
        # 表单验证
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            try:
                userForm.instance.password = make_password(userForm.cleaned_data['password'])
                userForm.save()
                msg = {"code": 0, "result": "添加用户成功", }
            except:
                logging.error("error is useradd")
                msg = {"code": 1, "result": "添加用户失败，请联系管理员"}
        else:
            msg = {"code": 1, "errmsg": userForm.errors}
        return render(request, "users/users_add.html", msg)
# 修改用户
class UserMod(LoginRequiredMixin,PermissionRequiredMixin, DetailView):
    template_name = "users/users_add.html"
    model = User
    permission_required = ['users.change_userprofile', 'users.add_userprofile']
    # 不可修改amdin
    def get_queryset(self):
        queryset = super(UserMod, self).get_queryset()
        queryset = queryset.exclude(username__icontains="admin")
        return queryset

    def post(self, request, **kwargs):
        msg = {}
        pk = kwargs.get("pk")
        user = self.model.objects.get(pk=pk)
        # 表单验证 instance=user指定
        userForm = UserForm(request.POST, instance=user)
        if userForm.is_valid():
            try:
                userForm.instance.password = make_password(userForm.cleaned_data['password'])
                userForm.save()
                msg = {"code": 0, 'object': self.model.objects.get(pk=pk), "result": "修改用户成功"}
            except:
                logging.error("error is useradd")
                msg = {"code": 1, "errmsg": "修改用户失败，请联系管理员"}
        else:
            msg = {"code": 1, 'object': self.model.objects.get(pk=pk), "errmsg": userForm.errors }
        return render(request, "users/users_add.html", msg)
# 用户添加用户组（角色）
class User_Add_Group(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    批量将用户添加到组
    """
    permission_required = 'users.change_userprofile'
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        groups = Group.objects.all()
        context = {'user': user, 'groups': groups}
        return render(request, 'users/user_add_group.html', context=context)

    def post(self, request, pk):
        gids = request.POST.getlist('groups')
        user = get_object_or_404(User, pk=pk)
        if gids:
            groups = Group.objects.filter(id__in=gids)
            user.groups.set(groups)
        else:
            user.groups.clear()
        messages.success(request, '{}修改所属组成功！'.format(user))
        return HttpResponseRedirect(reverse('users:user_add_group', kwargs={'pk': pk}))
# 用户添加权限
class Users_Add_Permission(LoginRequiredMixin, PermissionRequiredMixin, View):
        """
        用户添加权限
        """
        permission_required = 'users.change_userprofile'
        def get(self, request, pk):
            user = get_object_or_404(User, pk=pk)
            permissions = Permission.objects.exclude(Q(content_type__model='session') |
                                                     Q(content_type__model='contenttype') |
                                                     Q(content_type__model='logentry') |
                                                     Q(codename='add_permission') |
                                                     Q(codename='delete_permission') |
                                                     Q(codename='change_permission')
                                                     ).values('id', 'name',
                                                              'content_type__app_label',
                                                              'codename')
            context = {'user': user, 'permissions': permissions}
            return render(request, 'users/user_updata_permission.html', context=context)

        def post(self, request, pk):
            permissions = request.POST.getlist('permissions')
            print(permissions)
            user = get_object_or_404(User, pk=pk)
            if permissions:
                print(user.user_permissions.all())
                permissions = Permission.objects.filter(id__in=permissions)
                print(permissions)
                user.user_permissions.set(permissions)
                print(user.user_permissions.all())
                messages.success(request, '{}修改权限成功！'.format(user))
            else:
                user.groups.clear()
                messages.success(request, '{}清除权限成功！'.format(user))

            return HttpResponseRedirect(reverse('users:users_add_permission', kwargs={'pk': pk}))
# 删除用户
class UserDel(LoginRequiredMixin,PermissionRequiredMixin, View):
    permission_required = 'users.delete_userprofile'


    def post(self, request):
        pk = request.POST.get('id')
        try:
            user = User.objects.filter(pk=pk)
            user.delete()
            msg = {"code": 0, 'result': "删除用户成功"}
        except:
            logging.error("error is userdel")
            msg = {"code": 1, 'result': "删除用户失败,请联系维护人员"}
        return JsonResponse(msg)
# 激活
class Is_Active(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin, DetailView):
    template_name = "users/users_is_active.html"
    model = User
    permission_required = ['users.change_userprofile',]

    def post(self, request, **kwargs):
        msg = {}
        pk = kwargs.get("pk")
        user = self.model.objects.get(pk=pk)
        # 表单验证 instance=user指定
        is_active = request.POST.get('is_active')
        if is_active:
            try:
                user.is_active = is_active
                user.save()
                msg = {"code": 0, 'object': user, "result": "修改用户激活状态成功"}
            except:
                logging.error("error is is_active")
                msg = {"code": 1, "errmsg": "激活失败，请联系管理员"}
        else:
            msg = {"code": 1, 'object': self.model.objects.get(pk=pk), "errmsg": "激活失败，请联系管理员！"}
        return render(request, "users/users_is_active.html", msg)





class Test(TemplateView):
    template_name = "users/test.html"



