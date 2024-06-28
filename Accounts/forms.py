from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'input'}), initial='password')

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets ={
            'username': forms.TextInput(attrs={'class':'input'}),
            'email': forms.EmailInput(attrs={'class':'input'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'id':'SignUpName',
            'class':'form-control form-control-lg',
            'placeholder':'Enter your Name'
        })
        self.fields['email'].widget.attrs.update({
            'id':'SignUpEmail',
            'class':'form-control form-control-lg',
            'placeholder':'Enter your email'
        })
        self.fields['password'].widget.attrs.update({
            'id':'SignUpPassword',
            'class':'form-control form-control-lg',
            'placeholder':'Enter your password'
        })