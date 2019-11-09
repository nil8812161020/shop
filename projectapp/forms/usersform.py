from django import forms
from projectapp.models import Users

class UsersForm(forms.ModelForm):
    password = forms.CharField(max_length=60, widget=forms.PasswordInput,label='رمز عبور')
    class Meta:
        model=Users
        fields=['first_lastname','username','password','mobile','email']
        labels={
            'first_lastname':'نام و نام خانوادگی',
            'username':'نام کاربری',
            'mobile':'موبایل',
            'email':'پست الکترونیک'

           }
