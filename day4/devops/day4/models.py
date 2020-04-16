from django.db import models

class Day4(models.Model):
    SEX = (
        (0,'男'),
        (1,'女'),
    )
    SKILL = (
        (0,'Python'),
        (1,'Java'),
        (2,'PHP'),
        (3,'C#'),
    )
    name = models.CharField(max_length = 20,help_text='用户名')
    password = models.CharField(max_length=32,help_text="密码")
    tel = models.CharField(max_length=11,help_text="电话")
    email = models.CharField(max_length=35,help_text="邮箱")
    sex = models.IntegerField(choices = SEX,null=True,blank=True)
    skill = models.IntegerField(choices=SKILL, null=True, blank=True)
    def __str__(self):
        return self.name
