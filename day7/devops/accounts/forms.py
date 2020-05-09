from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required': '用户名不能为空'})
    password = forms.CharField(required=True, error_messages={'required': '密码不能为空'})


class PasswordForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required': '用户名不能为空'})
    password = forms.CharField(required=True, error_messages={'required': '密码不能为空'})
    # 二次确认密码是否一致
    new_password = forms.CharField(required=True, error_messages={'required': '新密码不能为空'})
    confirm_password = forms.CharField(required=True, error_messages={'required': '新密码不能为空'})

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get("new_password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if new_password != confirm_password:
            raise forms.ValidationError(
                "两次输入的新密码不一致",
                code="password_mismatch"
            )
        return confirm_password