from django import forms


class ProjectForm(forms.Form):
    title = forms.CharField(
        max_length=120
    )

    description = forms.CharField(
        max_length=1000,
        initial='Test'
    )
