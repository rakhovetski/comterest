from django import forms

from account.models import Role
from team.models import Team


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

    class Meta:
        model = Team
        fields = ('title', 'description', 'role',)