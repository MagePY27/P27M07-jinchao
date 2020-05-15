from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import logging
# 调入数据表
from Pj_information.models import P_information
# 引用相关模版
from django.views.generic import TemplateView, ListView, DeleteView, DetailView
from django.http import HttpResponse
# 表单验证
from Pj_information.form import InformationForm
from django.shortcuts import reverse
from django.http import HttpResponseRedirect, JsonResponse





class InformationList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "Pj_information.view_p_information"
    template_name = "Pj_information/information_list.html"
    model = P_information
    context_object_name = "users"
    # index页面传来get请求中如果有add则转入添加页面

    # 删除信息
    def post(self, request):
        pk = request.POST.get('id')
        try:
            user = self.model.objects.filter(pk=pk)
            user.delete()
            msg = {"code": 0, 'result': "删除成功"}
        except:
            logging.error("error is userdel")
            msg = {"code": 1, 'result': "删除失败,请联系维护人员"}
        return JsonResponse(msg)

class InformationAdd(LoginRequiredMixin,TemplateView):
    template_name = "Pj_information/information_add.html"
    # 将添加页面传到后端的数据添加到数据库
    def post(self, request):
        msg = {}
        html = 'Pj_information/information_add.html'
        # 点击确认时，进行添加用户操作
        if "_save" in request.POST:
            # 表单验证
            userForm = InformationForm(request.POST)
            if userForm.is_valid():
                # 验证通过，使用表单写入数据库
                try:
                    userForm.save()
                    msg = {"code": 0, "result": "添加成功", }
                except:
                    logging.error("error is useradd")
                    msg = {"code": 1, "errmsg": "添加失败，请联系管理员", }
            else:
                print(InformationForm.errors)
                msg = {"code": 1, 'errmsg': userForm.errors}
        # 点击返回时，定义返回页面
        if "_return" in request.POST:
            html = "Pj_information/information_list.html"
            msg = {"users": P_information.objects.all()}
        return render(request, html, msg)

class InforMod(LoginRequiredMixin, DetailView):
    # 输出数据到指定页面
    template_name = "Pj_information/information_add.html"
    # 指定数据表信息
    model = P_information
    def post(self,request,**kwargs):
        pk = kwargs.get("pk")
        html = 'Pj_information/information_add.html'
        msg = {}
        if "_save" in request.POST:
            user = self.model.objects.get(pk=pk)
            userForm = InformationForm(request.POST,instance=user)
            if userForm.is_valid():
                try:
                    userForm.save()
                    msg = {"object": self.model.objects.get(pk=pk), "code": 0, "result": "更新用户信息成功", }
                except:
                    logging.error("error is usermod")
                    msg = {"code": 1, "errmsg": "更细用户信息失败，请联系管理员", }
            else:
                logging.error("error is usermod new")
                msg = {"code": 1, 'errmsg': userForm.errors}
        elif "_return" in request.POST:
            html = "Pj_information/information_list.html"
            msg = {"users": P_information.objects.all()}
        else:
            logging.error("error  not requesr.POST")
        return render(request, html, msg)

class UserDel(LoginRequiredMixin, DeleteView):
    template_name = "Pj_information/information_del.html"
    model = P_information
    context_object_name = "user"
    def post(self, request,**kwargs):
        if "_save" in request.POST:
            pk = kwargs.get("pk")
            user = self.model.objects.get(pk=pk)
            user.delete()

        return render(request, "Pj_information/information_list.html", {"users": P_information.objects.all()} )


