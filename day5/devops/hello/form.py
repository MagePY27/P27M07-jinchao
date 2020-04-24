from django import forms
from hello.models import User
import re

class UserModelForm(forms.ModelForm):
    """
    验证密码合法性
    """
    # 二次确认密码是否一致
    confirm_password = forms.CharField(required=True)

    class Meta:
        model = User
        fields = "__all__"

    def clean_phone(self):
        """
         正则验证手机号码合法性，首写1 第二位是【34578】任一位 后九位为0-9任意
        """
        phone = self.cleaned_data['phone']
        phone_regex = r"^1[34578][0-9]{9}$"
        #判断是否合法对应不同输出 ,不符合要求抛出异常
        p = re.compile(phone_regex)
        if p.match(phone):
            return phone
        else:
            raise forms.ValidationError("手机号码非法，请输出正确手机号码",code = "invalid")

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if len(password) < 6:
            raise forms.ValidationError(
                "密码不能少于6位数",
                code="password_mismatch"
            )
        if password != confirm_password:
            raise forms.ValidationError(
                "两次输入的密码不一致",
                code = "password_mismatch"
            )
        return confirm_password

