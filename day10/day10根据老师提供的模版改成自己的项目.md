# ����ģ������Լ�����Ŀ

### �ʲ�չʾ
- ��̨����ƴ�ӷ��ص�ǰ��
~~~
class Overview(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'host.view_tag'
    """
    �ʲ�չʾ
    """
    def get(self, request):
        # ��Ŀʡ�ݷֲ���Ϣ���ֵ�����ʽ�����б�����ʽ��
        overview = {"{}_assets_count".format(type.name): [{"name": tag.name_cn, "value": len(tag.host_set.all())} for tag in type.tag_set.all()] for type in Type.objects.all()}
        
        # ���������Ϣ����û�����ô�ĳ�����ʽ��ʽ��
        overview1 = {}
        for type in Type.objects.all():
            status_Running = status_Error = pstatus_Error = 0
            for tag in type.tag_set.all():
                status_Running = status_Running + len(tag.host_set.filter(status='Running'))
                status_Error = status_Error + len(tag.host_set.filter(status='Error'))
                pstatus_Error = pstatus_Error + len(tag.host_set.filter(pstatus='Error'))
            function_count = [{"name": '����������', 'value': status_Error}, {"name": '�������', 'value': pstatus_Error}, {"name": '����', 'value': status_Running}]
            overview1["{}_function_count".format(type.name)] = function_count
        
        # ƴ���ֵ䣬����context
        overview.update(overview1)
        context = {
            'overview': overview,
        }
        return render(request, "cmdb/assets_overview.html", context=context)================
~~~
- Ч����ͼ
![�ʲ�չʾ1](G:\pythonʵս\pythonʵս\day10\�ʲ�չʾ1.png)
![�ʲ�չʾ2](G:\pythonʵս\pythonʵս\day10\�ʲ�չʾ2.png)


- �ʲ��б�չʾ������ʱ���ϵ�����չʾ��Ŀ���󵼺���չʾ��Ŀ���ƣ����չʾ��Ŀ�ſ���������ͼ��
![����1](G:\pythonʵս\pythonʵս\day10\����1.png)
![�������ѡ����Ŀʱ](G:\pythonʵս\pythonʵս\day10\�������ѡ����Ŀʱ.png)


- �ʲ��б�չʾ��չʾ������Ŀ��Ϣʱ�󵼺���Ϊ�ֵ���Ϣ�����Ϊ���������飨������ͼ��
![չʾ��Ŀ��Ϣ](G:\pythonʵս\pythonʵս\day10\չʾ��Ŀ��Ϣ.png)
![չʾ��Ŀ��Ϣ�ֵ�ʱ����ɸѡ](G:\pythonʵս\pythonʵս\day10\չʾ��Ŀ��Ϣ�ֵ�ʱ����ɸѡ.png)

- ����Ŀ���ʱ���ϵ������Զ���չ��������Ŀ�б��������Ŀʱ����Դ��Ϣ�ϵ������Զ���չ����ͼ��
![������Ŀ���Զ���չ��Ŀ��Ϣ�ϵ�����](G:\pythonʵս\pythonʵս\day10\������Ŀ���Զ���չ��Ŀ��Ϣ�ϵ�����.png)





