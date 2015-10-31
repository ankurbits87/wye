from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from . import models


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label=_("Email"), max_length=100, required=True)
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput,
                               required=True)


class SignupForm(forms.ModelForm):
    mobile = forms.CharField(label=_("Mobile"), max_length=10,
                             required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }

    def save(self, user):
        user.profile.mobile = self.cleaned_data['mobile']
        user.save()


class UserProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.Profile
        exclude = ('user', 'slug')
