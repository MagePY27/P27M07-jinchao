from django.db import models

class User(models.Model):
    SEX = (
        (0,'男'),
        (1,'女'),
    )
    user = models.CharField(max_length=10,help_text='用户名')
    name = models.CharField(max_length = 10,help_text='姓名')
    phone = models.CharField(max_length= 11, help_text="手机")
    password = models.CharField(max_length=32,help_text="密码")
    sex = models.IntegerField(choices = SEX,null=True,blank=True)
    def __str__(self):
        return self.name







