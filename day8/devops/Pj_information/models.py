from django.db import models

from django.db import models

class P_information(models.Model):
    # 设置项目状态
    STATE = (
        (0, "正在进行"),
        (1, "失败"),
        (2, "延迟"),
        (3, "完成"),
    )
    # 项目类型
    TYPE = (
        (0, "故障"),
        (1, "BUG"),
        (2, "需求"),
        (3, "逾期|放弃"),
    )
    # 记录信息名称,字符串字段
    name = models.CharField(max_length=20, help_text="项目名称")
    # 项目类型
    project_type = models.IntegerField(choices=TYPE, null=True, blank=True)
    # 首次创建时间默认为首次创建时间，后续不可更改
    start_date = models.DateField(auto_now_add=True, help_text="开始时间")
    # 结束时间，设置普通字符串
    end_date = models.CharField(max_length=25, help_text="结束时间")
    # 主要负责人
    res_name = models.CharField(max_length=20, help_text="主要负责人")
    # 项目备注， 设置为容量大的文本字段 TextField
    remarks = models.TextField(blank=True, help_text="项目状态")
    # 项目状态
    state = models.IntegerField(choices=STATE, null=True, blank=True)

    def __str__(self):
        return self.name
