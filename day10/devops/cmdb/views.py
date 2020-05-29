from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from cmdb.models import Tag, Type, Host

# 项目信息增删改查
class TypeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    项目信息列表
    """
    model = Type
    permission_required = 'cmdb.view_type'
    context_object_name = "types"
class TypeAddView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """
    创建项目
    """
    model = Type
    fields = ('name', 'name_cn', 'project_type')
    permission_required = 'cmdb.add_type'
    success_message = '添加 %(name)s 项目成功'
    def get_success_url(self):
        return reverse('cmdb:type-add')
class TypeEditView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    编辑项目
    """
    model = Type
    fields = ('name', 'name_cn', 'project_type')
    permission_required = 'cmdb.change_type'
    success_message = '项目 %(name_cn)s 编辑成功！'
    def get_success_url(self):
        return reverse('cmdb:type-edit', kwargs={'pk': self.object.pk})
class TypeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    删除项目
    """
    model = Type
    permission_required = 'cmdb.delete_type'

    def get_success_url(self):
        return reverse_lazy('cmdb:types')


# 标签增删改查
class TagListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    标签列表
    """
    model = Tag
    permission_required = 'cmdb.view_tag'
    context_object_name = "tags"
class TagAddView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """
    创建标签
    """
    model = Tag
    fields = ('type', 'name', 'name_cn')
    permission_required = 'cmdb.add_tag'
    success_message = '添加 %(name_cn)s 标签成功~'

    def get_success_url(self):
        return reverse('cmdb:tag-add')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        types = Type.objects.all()
        context['types'] = types
        return context
class TagEditView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    编辑省份
    """
    model = Tag
    fields = ('type', 'name', 'name_cn')
    permission_required = 'cmdb.change_tag'
    success_message = '%(name_cn)s 标签编辑成功！'

    def get_success_url(self):
        return reverse('cmdb:tag-edit', kwargs={'pk': self.object.pk})
    # 增加返回信息中所属项目信息
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context
class TagDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    删除标签
    """
    model = Tag
    permission_required = 'cmdb.delete_tag'
    def get_success_url(self):
        return reverse_lazy('cmdb:tags')
class Add_HostsView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    省份添加服务器
    """
    permission_required = 'cmdb.change_tag'

    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        hosts = Host.objects.all()
        context = {'tag': tag, 'hosts': hosts}
        return render(request, 'cmdb/tag_add_host.html', context=context)

    def post(self, request, pk):
        hosts = request.POST.getlist('hosts')
        tag = get_object_or_404(Tag, pk=pk)
        if hosts:
            hosts = Host.objects.filter(id__in=hosts)
            tag.host_set.set(hosts)
        else:
            hosts.user_set.clear()
        messages.success(request, '{}服务器更新成功！'.format(tag))
        return HttpResponseRedirect(reverse('cmdb:add-hosts', kwargs={'pk': pk}))


# 展示
class Hosts(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
        资源管理
        """
    model = Tag
    permission_required = 'host.view_tag'
    template_name = "cmdb/host_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        t = self.request.GET.get('type')
        if t:
            type = Type.objects.get(id=t)
            context['object_list'] = type.tag_set.all()
        context['types'] = Type.objects.all()
        return context
class Hosts_p(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    """
    资源管理
    """
    permission_required = 'host.view_tag'
    template_name = "cmdb/host_list_P.html"


    def get(self, request, *args, **kwargs):

        context = {}
        pk = kwargs['pk']
        # 当前项目信息
        context['type_p'] = Type.objects.get(id=pk)
        # 当前项目内省份
        context['tags'] = Type.objects.get(id=pk).tag_set.all()
        # 项目数目
        context['types'] = Type.objects.all()

        # 返回项目内所有的主机
        tags = Type.objects.get(id=pk).tag_set.all()
        hosts = Host.objects.none()
        for tag in tags:
            hosts = hosts | tag.host_set.all()
        context['object_list'] = hosts.distinct()

        # 点击省份信息时，返回对应的主机
        tag = self.request.GET.get('tag')
        if tag:
            tag = Tag.objects.get(id=tag)
            context['object_list'] = tag.host_set.all()
        return render(request, "cmdb/host_list_P.html", context=context)
class Overview(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'host.view_tag'
    """
    资产展示
    """
    def get(self, request):
        # 项目省份分布信息
        overview = {"{}_assets_count".format(type.name): [{"name": tag.name_cn, "value": len(tag.host_set.all())} for tag in type.tag_set.all()] for type in Type.objects.all()}
        # 故障情况信息
        overview1 = {}
        for type in Type.objects.all():
            status_Running = status_Error = pstatus_Error = 0
            for tag in type.tag_set.all():
                status_Running = status_Running + len(tag.host_set.filter(status='Running'))
                status_Error = status_Error + len(tag.host_set.filter(status='Error'))
                pstatus_Error = pstatus_Error + len(tag.host_set.filter(pstatus='Error'))
            function_count = [{"name": '服务器故障', 'value': status_Error}, {"name": '软件故障', 'value': pstatus_Error}, {"name": '正常', 'value': status_Running}]
            overview1["{}_function_count".format(type.name)] = function_count
        # 拼接字典，返回context
        overview.update(overview1)
        context = {
            'overview': overview,
        }
        return render(request, "cmdb/assets_overview.html", context=context)






