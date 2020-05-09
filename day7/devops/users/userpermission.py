from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView ,DetailView
from django.contrib.auth.models import Group, Permission
import logging
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

class UserPermission(ListView):
    template_name = "users/users_permission.html"
    model = Permission
    # permission_required = "auth.view_"
    context_object_name = "users"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(content_type__model__in=['logentry', 'session', 'contenttypr'])

        return queryset

class UserPermissionUpdata(DetailView):
    template_name = "users/users_permission_update.html"
    model = Permission
    context_object_name = "user"

    def post(self, request, **kwargs):
        msg = {}
        html = "users/users_permission_update.html"
        # 点击确认 修改数据库信息
        if "_save" in request.POST:
            try:
                pk = kwargs.get("pk")
                user = self.model.objects.get(pk=pk)
                user.name = request.POST.get('name')
                user.save()
                msg = {"code": 0, 'object': self.model.objects.get(pk=pk), "result": "修改成功"}
            except:
                logging.error("error is useradd")
                msg = {"code": 1, "errmsg": "修改失败，请联系维护人员"}
            return render(request, html, msg)
        if "_return" in request.POST:
            return HttpResponseRedirect('/userpermission/')