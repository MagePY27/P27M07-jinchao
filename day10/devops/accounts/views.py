from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView
from django.views.generic.base import View, TemplateView
from django.views.generic import DetailView


from accounts.forms import LoginForm, PasswordForm

User = get_user_model()


# Create your views here.
class LoginView(View):
    """
    登录
    """
    def get(self, request):
        login_form = LoginForm()
        return render(request, "account/login.html", {'login_form': login_form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                if user.is_active:
                    # print("111111111111111")
                    login(request, user)
                    return HttpResponseRedirect(reverse('users:index'))
                else:
                    return render(request, 'account/login.html', {'form': form, 'msg': '用户未激活！'})
            else:
                return render(request, 'account/login.html', {'form': form, 'msg': '用户名或密码错误！'})
        else:
            return render(request, 'account/login.html', {'form': form})


# 用户修改密码
class PasswordMod(LoginRequiredMixin, DetailView):
    template_name = 'account/passwordmod.html'
    model = User

    def post(self, request, **kwargs):
        msg = {}
        html = 'account/passwordmod.html'
        # 点击确认 修改数据库信息
        if "_save" in request.POST:
            pk = kwargs.get("pk")
            form = PasswordForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user:
                    user.password = make_password(form.cleaned_data['new_password'])
                    user.save()
                    msg = {"code": 0, 'object': self.model.objects.get(pk=pk), 'msgok': '密码已成功修改'}
                else:
                    msg = {'object': self.model.objects.get(pk=pk), 'form': form, 'msg': '密码错误！请确认密码'}
            else:
                msg = {"code": 1, 'object': self.model.objects.get(pk=pk), "form": form}
        # 点击返回 回到列表页面
        if "_return" in request.POST:
            html = "index.html"
        return render(request, html, msg)


class LogoutView(View):
    """
    用户退出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("accounts:login"))