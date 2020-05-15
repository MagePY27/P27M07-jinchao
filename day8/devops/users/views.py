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
from django.shortcuts import render
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

    def get_queryset(self):
        queryset = super(UserList, self).get_queryset()
        # 不显示amdin
        queryset = queryset.exclude(username__icontains="admin")
        self.keyword = self.request.GET.get("keyword", "").strip()
        if self.keyword:
            queryset = queryset.filter(Q(username__icontains=self.keyword) |
                                       Q(name__icontains=self.keyword)
                                       )
        return queryset
# 添加用户
class UserAdd(LoginRequiredMixin,PermissionRequiredMixin, TemplateView):
    permission_required = "users.add_userprofile"
    template_name = "users/users_add.html"
    def post(self, request):
        msg = {}
        html = "users/users_add.html"
        # 点击确认时，进行添加用户操作
        if "_save" in request.POST:
            # 表单验证
            userForm = UserForm(request.POST)
            if userForm.is_valid():
                try:
                    userForm.instance.password = make_password(userForm.cleaned_data['password'])
                    userForm.instance.is_active = 1
                    print(userForm.instance)
                    userForm.save()
                    msg = {"code": 0, "result": "添加用户成功", }
                except:
                    logging.error("error is useradd")
                    msg = {"code": 1, "errmsg": "添加用户失败，请联系管理员"}
            else:
                msg = {"code": 1, "errmsg": userForm.errors}
        # 点击返回时，返回列表页
        if "_return" in request.POST:
            html = "users/users_list.html"
            msg['users'] = User.objects.exclude(username__icontains="admin")
        return render(request, html, msg)
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
        html = "users/users_add.html"
        # 点击确认 修改数据库信息
        if "_save" in request.POST:
            pk = kwargs.get("pk")
            user = self.model.objects.get(pk=pk)
            # 表单验证 instance=user指定
            userForm = UserForm(request.POST, instance=user)
            if userForm.is_valid():
                try:
                    userForm.instance.password = make_password(userForm.cleaned_data['password'])
                    userForm.instance.is_active = 1
                    userForm.save()
                    msg = {"code": 0, 'object': self.model.objects.get(pk=pk), "result": "修改用户成功"}
                except:
                    logging.error("error is useradd")
                    msg = {"code": 1, "errmsg": "修改用户失败，请联系管理员"}
            else:
                msg = {"code": 1, 'object': self.model.objects.get(pk=pk), "errmsg": userForm.errors }
        # 点击返回 回到列表页面
        if "_return" in request.POST:
            html = "users/users_list.html"
            msg['users'] = User.objects.exclude(username__icontains="admin")
        return render(request, html, msg)

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

class Test(ListView):
    template_name = 'test.html'
    model = Group
    permission_required = 'auth.view_group'
    context_object_name = "users"






