from django import forms
from tracker.models import MyUser, Bug
from django.contrib.auth.forms import UserCreationForm



class BugForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea())

class SignupForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 
                  'displayname'
                )
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    

    