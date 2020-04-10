from django.http import HttpResponse
from django.shortcuts import render
from hello.models import User
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

#信息首页
class UserList(ListView):
    template_name =  'userlist.html'
    model = User
    context_object_name = 'users'
    keyword = ""
    def get_queryset(self):
        queryset = super(UserList,self).get_queryset()
        self.keyword = self.request.GET.get("keyword","")
        if self.keyword :
            queryset = queryset.filter(name__icontains=self.keyword)
        return queryset
#新增用户
class UserAdd(CreateView):
    template_name = 'hello/useradd.html'
    model = User
    fields = ('name','password','sex')
    def get_success_url(self):
        return reversed(userlist)
    def post(self, request):
            data = request.POST.dict()
            print(data)
            User.objects.create(**data)
            users = User.objects.all()
            return render(request, 'userlist.html', {"users": users})
#修改用户信息
class UserMod(UpdateView):
    template_name = 'hello/usermod.html'
    model = User
    context_object_name = 'user'
    fields = ('name','password','sex')
    def post(self, request, *args, **kwargs):
        data = request.POST.dict()
        User.objects.filter(id=request.POST.get('id')).update(**data)
        users = User.objects.all()
        return render(request,'userlist.html',{"users":users})
#删除用户信息
class UserDel(DeleteView):
    model = User
    template_name = 'hello/userdel.html'
    context_object_name = 'users'
    def post(self, request, *args, **kwargs):
        print(kwargs)
        User.objects.get(pk=kwargs.get('pk')).delete()
        users = User.objects.all()
        return render(request,'userlist.html',{"users":users})
















    #将数据库数据以users为key添加
    # def get_context_data(self, **kwargs):
    #     context = super(UserDel, self).get_context_data(**kwargs)
    #     context['users'] = User.objects.all()
    #     return context