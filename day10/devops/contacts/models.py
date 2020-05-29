from django.db import models

"""
安全中心联系人
"""
class Contacts(models.Model):
    """
    主机基本信息
    """
    SEX = (
        (0, '男'),
        (1, '女'),
    )
    TYPE = (
        (0, '客户'),
        (1, '友商'),
        (2, '内部')
    )
    name = models.CharField(max_length=22, verbose_name='联系人姓名')
    sex = models.IntegerField(choices=SEX, null=True, blank=True)
    occupation = models.CharField(max_length=22, verbose_name='职务')
    company = models.CharField(max_length=22, verbose_name='所属公司')
    project = models.CharField(max_length=22, verbose_name='所属项目')
    phone = models.CharField(max_length=11, null=True, blank=True,verbose_name='手机')
    type = models.IntegerField(choices=TYPE, default=0, verbose_name='联系人类别')

    class Meta:
        verbose_name = '联系人信息'

    def __str__(self):
        return self.name
