from django.db import models

#出版商表结构
class Publisher(models.Model):
    name = models.CharField(max_length= 30 )
    address = models.CharField(max_length=50)
    city = models.CharField(max_length= 60)

    def __str__(self):
        return self.name
#作者的表结构
class Author(models.Model):
    name   = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.name

#书的表结构
class Book(models.Model):
    ##构建书名与作者 书与作者是多对多的关系
    title = models.CharField(max_length=100,help_text="书名")
    authors = models.ManyToManyField(Author,verbose_name="作者",help_text='作者')
    ###设置外键 一本书只能被一家出版，出版商可以出版多本书
    publisher = models.ForeignKey(Publisher,verbose_name="出版社",help_text="出版社",on_delete=models.CASCADE)

    def __str__(self):
        return self.title
