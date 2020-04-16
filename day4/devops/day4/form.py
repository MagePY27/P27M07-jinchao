from django import forms
from day4.models import Day4

class UserForm(forms.Form):
    #定义最大最小值，默认不允许为空
    name = forms.CharField(max_length=10)
    password = forms.CharField(min_length=6,required=True)
    tel = forms.CharField(max_length=11,min_length=11,required=True)
    email = forms.CharField(max_length=32,required=True)
    file = forms.FileField(required=False)

    def clean_info(self):
        info = self.changed_data['info']
        print(info.split())
        num_info = len(info.split())
        if num_info <4 :
            raise forms.ValidationError('Info not enough words!')
        return info