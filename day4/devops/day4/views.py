from django.shortcuts import render
from django.shortcuts import reverse
from day4.models import Day4
from django.views.generic import ListView,DeleteView,UpdateView,TemplateView
from django.contrib.messages.views import SuccessMessageMixin
import os
from day4.form import UserForm

#列表筛选与添加
class UserList(SuccessMessageMixin,ListView):
    template_name = 'day4/index.html'
    model = Day4
    context_object_name = 'users'
    success_message = "%(name)s 添加成功！！！"
    #筛选
    def get_queryset(self):
        queryset = super(UserList,self).get_queryset()
        self.keyword = self.request.GET.get("keyword","")
        if self.keyword :
            print(queryset)
            queryset = queryset.filter(name__icontains=self.keyword)
            print(queryset)
        return queryset
    ##添加用户页面跳转
    def get_template_names(self):
        names = super().get_template_names()
        if 'add' in self.request.GET:
            names = ['day4/dayadd.html']
        return names
    ###添加用户
    def post(self, request):
        user_input_obj = UserForm(request.POST)
        print(user_input_obj)
        if user_input_obj.is_valid():
            #验证成功，文件上传
            file = request.FILES.get('file', None)
            if file:
                f = open(os.path.join('upload', file.name), 'wb')
                for line in file.chunks():
                    f.write(line)
                f.close()
        else:
            #验证失败返回验证信息
            form = user_input_obj.errors ##获取错误信息
            print(form)
            return render(request, 'day4/dayadd.html', {'form': form})
        self.html = 'day4/index.html'
        data = request.POST.dict()
        if '_save' in data:
            data.pop('_save')
            Day4.objects.create(**data)
            self.html = 'day4/dayadd.html'
        users = Day4.objects.all()
        return render(request, self.html,{"users": users})
#列表删除
class UserDel(DeleteView):
    model = Day4
    template_name = 'day4/daydel.html'
    def get_success_url(self):
        return reverse('day4:index')

#列表修改
class UserMod(SuccessMessageMixin,UpdateView):
    success_message = "%(name)s 修改成功！！！"
    template_name = 'day4/daymod.html'
    model = Day4
    context_object_name = 'user'
    fields = ('name','password','sex','tel','email','skill')
    def get_success_url(self):
        if 'return' in self.request.POST:
            return reverse('day4:index')










