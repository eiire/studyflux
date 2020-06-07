from django import forms


class ProjectForm(forms.Form):
    title = forms.CharField(
        max_length=120
    )
    description = forms.TextInput()
    technology = forms.CharField(
        max_length=30
    )
    github = forms.CharField(
        max_length=100
    )
    name_for_portfolios = forms.CharField(
        max_length=100,
        initial='Project'
    )
