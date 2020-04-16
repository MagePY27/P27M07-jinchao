from django.shortcuts import reverse,render
from django.views.generic import View, TemplateView
import os


class HtmlView(TemplateView):
    template_name = "hello/test.html"

    def post(self,request):
        print(request.POST)
        data = request.POST.dict()
        print(data)
        print(dict(request.POST))
        data1 = {k:",".join(v) for k,v in dict(request.POST).items()}
        print(data1)


        #接受文件
        file = request.FILES.get('file',None)
        print(file)
        print(type(file))
        if file:
            f = open(os.path.join('upload' ,file.name),'wb')
            for line in file.chunks():
                f.write(line)
            f.close()

        return render(request, 'hello/test.html')