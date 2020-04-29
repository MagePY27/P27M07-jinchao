from django.views.generic import ListView,DetailView,View,TemplateView
from hello.models import User
from django.shortcuts import render
from django.conf import settings
from hello.form import UserModelForm
import logging
from django.db.models import Q

# 首页
class IndexView(ListView):
    template_name = 'hello/index.html'
    # def get_template_names(self):
    #     template_name = super(IndexView,self).get_template_names()
    #     print(self.request.POST)
    #     # if 'add' in self.request.GET.dict():
    #     #     template_name= ['hello/useradd.html']
    #     return template_name


# 用户列表页
class UserList(ListView):
    model = User
    template_name = "hello/userlist.html"
    context_object_name = "users"
    # 通过keyword筛选用户
    def get_queryset(self):
        queryset = super(UserList,self).get_queryset()
        self.keyword = self.request.GET.get("keyword","").strip()
        if self.keyword:
            queryset = queryset.filter(Q(user__icontains=self.keyword)|
                                       Q(phone__icontains=self.keyword)|
                                       Q(name__icontains=self.keyword)
                                       )
        return queryset
    # 点击添加进入添加用户界面
    def get_template_names(self):
        template_name = super(UserList,self).get_template_names()
        if 'add' in self.request.GET.dict():
            template_name= ['hello/useradd.html']
        return template_name
    # post请求 添加用户时
    def post(self,request):
        msg = {}
        html = settings.JUMP_PAGE
        # 点击确认时，进行添加用户操作
        if "_save" in request.POST:
            #表单验证
            userForm = UserModelForm(request.POST)
            if userForm.is_valid():
                try:
                    userForm.save()
                    msg = {"code":0,"result":"添加用户成功",}
                except:
                    logging.error("error is useradd")
                    msg = {"code":1,"errmsg":"添加用户失败，请联系管理员"}
            else:
                msg = {"code":1,"errmsg":userForm.errors}
        # 点击返回时，返回列表页
        if "_addreturn" in request.POST:
            html = "hello/userlist.html"
            msg['users'] = User.objects.all()
        return render(request,html,msg)



class UserMod(DetailView):
    # 修改信息时 设置数据库与页面回馈
    template_name = "hello/usermod.html"
    model = User
    context_object_name = "user"

    # post请求操作
    def post(self,request,**kwargs):
        msg = {}
        html = settings.JUMP_PAGE
        # 点击确认 修改数据库信息
        if "_save" in request.POST:
            pk = kwargs.get("pk")
            user = self.model.objects.get(pk=pk)
            # 表单验证 instance=user指定
            userForm = UserModelForm(request.POST,instance=user)
            if userForm.is_valid():
                try:
                    userForm.save()
                    msg = {"code": 0, "result": "修改用户成功"}
                except:
                    logging.error("error is useradd")
                    msg = {"code": 1, "errmsg": "修改用户失败，请联系管理员"}
            else:
                msg = {"code": 1, "errmsg": userForm.errors}
        # 点击返回 回到列表页面
        if "_modreturn" in request.POST:
            html = "hello/userlist.html"
            msg['users'] = User.objects.all()

        print(request)
        return render(request,html,msg)

class UserDel(DetailView):
    # 修改信息时 设置数据库与页面回馈
    template_name = "hello/userdel.html"
    model = User
    context_object_name = "user"

    # post请求操作
    def post(self,request,**kwargs):
        msg = {}
        html = "hello/userlist.html"
        # 点击确认 修改数据库信息
        if "_save" in request.POST:
            try:
                pk = kwargs.get("pk")
                user = self.model.objects.get(pk=pk)
                # 表单验证 instance=user指定
                user.delete()
                msg['users'] = User.objects.all()

            except:
                html = settings.JUMP_PAGE
                msg = {"code": 1, "errmsg": "删除用户失败，请联系管理员"}

        if "_modreturn" in request.POST:
            msg['users'] = User.objects.all()
        return render(request,html,msg)



    #
    #         (View):
    # html = settings.JUMP_PAGE
    # msg = {}
    #
    # def get(self, request, **kwargs):
    #     try:
    #         pk = kwargs.get("pk")
    #         user = User.objects.all().get(pk=pk)
    #         print(user)
    #         # user.delete()
    #         self.msg = {"code": 0, "result": "删除用户成功"}
    #         self.msg['user'] = user
    #         html = "hello/userdel.html"
    #     except:
    #         self.msg = {"code": 1, "errmsg": "删除用户失败，请联系管理员"}
    #
    #     return render(request, self.html, self.msg)






#  界面html练习
class HtmlTest(TemplateView):
    template_name = "test.html"
    model = User





class IndexView(ListView):
    template_name = 'hello/index.html'
    model = User
    def get_template_names(self):
        template_name = super(IndexView,self).get_template_names()
        print(self.request.POST)
        # if 'add' in self.request.GET.dict():
        #     template_name= ['hello/useradd.html']
        return template_name

