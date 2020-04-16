# from django import forms
#
#
#
# class UserForm(forms.Form):
#     name = forms.CharField(max_length=10,reversed=True)
#     password = forms.CharField(max_length=10, reversed=True)
#     file= forms.FileField()
#     info = forms.CharField(max_length=100,reversed=True)
#     def clean_info(self):
#         info = self.changed_data['info']
#         print(info.split())
#         num_info = len(info.split())
#         if num_info <4 :
#             raise forms.ValidationError("info not enough words!")
#         return info