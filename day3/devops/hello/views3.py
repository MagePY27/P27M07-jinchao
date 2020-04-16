from django.shortcuts import reverse
from hello.models import User
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

class UserAdd(SuccessMessageMixin,CreateView):
    template_name = 'hello/useradd.html'
    model = User
    fields = ('name','password','sex')
    Success_message = "%(name)s was created successfully"
    def get_success_url(self):
        print(self.request.POST)
        if '_addanother' in self.request.POST:
            return reverse('hello:useradd')
        return reverse('hello:userlist')
class UserList(ListView):
    template_name =  'hello/userlist.html'
    model = User
    context_object_name = 'users'
#修改用户信息
class UserMod(UpdateView):
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