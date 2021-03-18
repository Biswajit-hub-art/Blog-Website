from django import forms
from django.contrib.auth import authenticate, logout

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100, label="Username")
#     password = forms.CharField(max_length=100, label="Password", widget=forms.PasswordInput)
#
#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#
#     if username and password:
#         user = authenticate(username=username, password=password)
#
#         if not user:
#             raise forms.ValidationError("Username or Password not correct")
#
#         super(LoginForm, self).clean()
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# register form
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
