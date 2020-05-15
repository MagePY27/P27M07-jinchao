from django import forms
from users.models import UserProfile
import re

class UserForm(forms.ModelForm):
    """
    验证密码合法性
    """
    class Meta:
        model = UserProfile
        fields = "__all__"

    date_joined = forms.CharField(required=False)
    # 二次确认密码是否一致
    confirm_password = forms.CharField(required=True)
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
                code="password_mismatch"
            )
        return confirm_password






