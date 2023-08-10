from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, PortfolioProject, Role, Team


class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label='Profile Picture')

    class Meta:
        model = Profile
        fields = ('profile_image',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PortfolioProjectForm(forms.ModelForm):
    title = forms.CharField(required=True,
                            widget=forms.widgets.Textarea(
                                attrs={
                                    'placeholder': 'Enter Project Title',
                                },
                            ), label='')
    description = forms.CharField(required=True,
                                  widget=forms.widgets.Textarea(
                                      attrs={
                                          'placeholder': 'Enter Description'
                                      },
                                  ), label='')
    role = forms.ModelMultipleChoiceField(queryset=Role.objects.all(),
                                          widget=forms.CheckboxSelectMultiple,
                                          required=True)

    class Meta:
        model = PortfolioProject
        exclude = ('user',)


class TeamForm(forms.ModelForm):
    title = forms.CharField(required=True,
                            widget=forms.widgets.Textarea(
                                attrs={
                                    'placeholder': 'Enter Team Name',
                                },
                            ), label='')
    description = forms.CharField(required=True,
                                  widget=forms.widgets.Textarea(
                                      attrs={
                                          'placeholder': 'Enter Description'
                                      },
                                  ), label='')
    role = forms.ModelMultipleChoiceField(queryset=Role.objects.all(),
                                          widget=forms.CheckboxSelectMultiple,
                                          required=True)
    profile = forms.ModelMultipleChoiceField(queryset=Profile.objects.all(),
                                             widget=forms.CheckboxSelectMultiple,
                                             required=True)

    class Meta:
        model = Team
        fields = ('title', 'description', 'role', 'profile')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    first_name = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span><small>Enter the same password as before, for verification.</small></span>'
