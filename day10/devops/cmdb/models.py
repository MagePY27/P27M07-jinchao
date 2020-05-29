from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
"""
安全中心项目资产整理
"""
class Type(models.Model):
    """
    标签类型，记录所属哪个项目
    """
    PROJECT_TYPE = (
        ('Develop', '开发中'),
        ('Maintain', '运维中')
    )
    name = models.CharField(max_length=100, verbose_name='涉密名称')
    name_cn = models.CharField(max_length=100, verbose_name='交流名称')
    project_type = models.CharField(max_length=16, default='Maintain', choices=PROJECT_TYPE, verbose_name='实例项目阶段')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '标签类型'
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = (
            ('view_type', '查看标签类型'),
            ('add_type', '添加标签类型'),
            ('change_type', '编辑标签类型'),
            ('delete_type', '删除标签类型'),
        )

    def __str__(self):
        return self.name_cn


class Tag(models.Model):
    """
    标签，记录所属哪个省份
    """
    type = models.ForeignKey('Type', verbose_name='类型', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='标签名称')
    name_cn = models.CharField(max_length=100, verbose_name='中文名称')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = (
            ('view_tag', '查看标签'),
            ('add_tag', '添加标签'),
            ('change_tag', '编辑标签'),
            ('delete_tag', '删除标签'),
        )

    def __str__(self):
        return self.name_cn


NETWORK = (
    ('z_network', 'Z网'),
    ('v_network', 'V网'),
)

class Host(models.Model):
    """
    主机基本信息
    """

    STATUS = (
        ('Running', '运行中'),
        ('Error', '异常'),
        ('Stopped', '已停止')
    )

    PSTATUS = (
        ('Running', '运行中'),
        ('Error', '异常'),
        ('Stopped', '已停止')
    )

    ip = models.GenericIPAddressField(blank=True, null=True, verbose_name='IP')
    public_network = models.CharField(max_length=20, choices=NETWORK, default='v_network', verbose_name='实例部署网络')
    name = models.CharField(max_length=22, verbose_name='实例的显示名称')
    description = models.CharField(max_length=128, null=True, blank=True, verbose_name='实例的描述')
    cpu = models.IntegerField(verbose_name='CPU核数')
    memory = models.IntegerField(verbose_name='内存大小，单位: GB')
    status = models.CharField(max_length=8, choices=STATUS, default='Running', verbose_name='实例状态')
    pstatus = models.CharField(max_length=8, choices=PSTATUS, default='Running', verbose_name='实例部署项目软件状态')
    hostname = models.CharField(max_length=23, blank=True, null=True, verbose_name='实例机器名称')
    os_type = models.CharField(max_length=10, default='linux', verbose_name='操作系统类型')
    os_name = models.CharField(max_length=20, default='', verbose_name='操作系统名称')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='入库时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    # 软件版本
    #


    class Meta:
        verbose_name = '主机'
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = (
            ('view_host', '查看主机'),
            ('change_host', '更新主机信息'),
        )

    def __str__(self):
        return self.name
