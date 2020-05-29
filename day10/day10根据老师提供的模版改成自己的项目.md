# 根据模版完成自己的项目

### 资产展示
- 后台数据拼接返回到前端
~~~
class Overview(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'host.view_tag'
    """
    资产展示
    """
    def get(self, request):
        # 项目省份分布信息（字典生成式内套列表生成式）
        overview = {"{}_assets_count".format(type.name): [{"name": tag.name_cn, "value": len(tag.host_set.all())} for tag in type.tag_set.all()] for type in Type.objects.all()}
        
        # 故障情况信息（还没想好怎么改成生成式格式）
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
        return render(request, "cmdb/assets_overview.html", context=context)================
~~~
- 效果如图
![资产展示1](G:\python实战\python实战\day10\资产展示1.png)
![资产展示2](G:\python实战\python实战\day10\资产展示2.png)


- 资产列表展示。总览时，上导航栏展示项目，左导航栏展示项目名称，表格展示项目概况（具体如图）
![总览1](G:\python实战\python实战\day10\总览1.png)
![总览点击选择项目时](G:\python实战\python实战\day10\总览点击选择项目时.png)


- 资产列表展示。展示具体项目信息时左导航栏为局点信息，表格为服务器详情（具体如图）
![展示项目信息](G:\python实战\python实战\day10\展示项目信息.png)
![展示项目信息局点时进行筛选](G:\python实战\python实战\day10\展示项目信息局点时进行筛选.png)

- 新项目添加时，上导航栏自动扩展，当对项目列表添加新项目时，资源信息上导航栏自动扩展（如图）
![增加项目后自动扩展项目信息上导航栏](G:\python实战\python实战\day10\增加项目后自动扩展项目信息上导航栏.png)





