from django import forms
from .models import Profile,Image,Comment,Like
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['followers','following','user']

class PostImage(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['owner','post_date','profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','image','posted_on']

class UpdateImage(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image','owner','profile','post_date']