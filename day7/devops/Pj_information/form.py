from django import forms
from Pj_information.models import P_information
import  re

class InformationForm(forms.ModelForm):
    """
    表单验证，对前端传来的数据进行验证，避免数据库报错对数据库造成压力
    """
    # 继承数据库的所有验证信息
    class Meta:
        model = P_information
        fields = "__all__"
    # 自定义相关的表单验证
    # 记录信息名称,最长20，不能为空
    name = forms.CharField(max_length=20, help_text="sadasdasfdasfaf")

    # 主要负责人  主要负责人最长为15字符，默认不能为空
    res_name = forms.CharField(max_length=15, )

    # 项目备注， 最大400字,可以为空
    remarks = forms.CharField(max_length=400, required=False)

    # 结束时间可以为空
    end_date = forms.CharField(required=False)

    # ｛创建时间：自动生成无需验证｝｛项目状态：前端使用选择器默认正在进行｝
    # start_dat  state


