from django import forms
class ForgotPassword(forms.Form):
    username=forms.CharField(label="username",required=True)

class LoginForm(forms.Form):
    username=forms.CharField(label="username",required=True)
    password=forms.CharField(label="Password",  widget=forms.PasswordInput)
class RegisterForm(forms.Form):
    username=forms.CharField(label="UserName",required=False)
    name = forms.CharField(label="Name",required=False)
    email = forms.CharField(label="email",required=False)
    password=forms.CharField(label="Password",  widget=forms.PasswordInput,required=False)
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        email=self.cleaned_data.get("email")
        name=self.cleaned_data.get("name")
        values = {
            "username" : username,
            "password" : password,
            "name":name,
            "email":email
        }
        return values
