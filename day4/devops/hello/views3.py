from django.shortcuts import reverse
from hello.models import User
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
#from hello.form import UserForm
from django.http import HttpResponse,HttpResponseRedirect

class UserAdd(SuccessMessageMixin,CreateView):
    template_name = 'hello/useradd.html'
    model = User
    fields = ('name','password','sex')

#成功输出
    success_message = "%(name)s 添加成功！！！"
    def get_success_url(self):
        if '_addreturn' in self.request.POST:
            return reverse('hello:userlist')
        return reverse('hello:useradd')
#错误输出
    def form_invalid(self, form):
        if form:
            return self.render_to_response(self.get_context_data(form=form))
class UserList(ListView):
    template_name =  'hello/userlist.html'
    model = User
    context_object_name = 'users'
#筛选
    def get_queryset(self):
        queryset = super(UserList, self).get_queryset()
        keyword = self.request.GET.get("keyword", "")
        if self.keyword:
            queryset = queryset.filter(name__icontains=self.keyword)
        return queryset

#修改用户信息
class UserMod(SuccessMessageMixin,UpdateView):
    success_message = "%(name)s 修改成功！！！"
    template_name = 'hello/usermod.html'
    model = User
    context_object_name = 'user'
    fields = ('name','password','sex')
    def get_success_url(self):
        if '_modout' in self.request.POST:
            return reverse('hello:userlist')
#删除用户信息
class UserDel(DeleteView):
    model = User
    template_name = 'hello/userdel.html'
    def get_success_url(self):
        return reverse('hello:userlist')









