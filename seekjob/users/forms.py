from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileRegisterForm(forms.ModelForm):
    class_number = forms.CharField(max_length=10)

    CAREER_PATH_CHOICES = [
        ('IT', 'IT'),
        ('FIN', 'Finance'),
        ('PHA', 'Pharmaceutical'),
        ('ACA', 'Academia'),
        ('OTH', 'Other')
    ]

    career_path = forms.ChoiceField(
        choices=CAREER_PATH_CHOICES
    )

    company = forms.CharField(
        required=False
    )

    employment_status = forms.ChoiceField(
        choices=(
            ('1', 'Looking for Jobs'),
            ('2', 'Looking for Candidates'),
            ('3', 'Both')
        )
    )

    start_time = forms.ChoiceField(
        choices=(
            ('1', 'In 2 weeks'),
            ('2', 'In a month'),
            ('3', 'In 3 months'),
            ('4', 'In 6 months')
        )
    )

    class Meta:
        model = Profile
        fields = ['class_number', 'career_path', 'company', 'employment_status', 'start_time']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'resume', 'class_number', 'career_path', 'company', 'employment_status',
                  'start_time']