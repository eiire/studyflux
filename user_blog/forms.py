from django import forms


class CommentForm(forms.Form):
    body = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'cols': '10', 'rows': '3', 'class': 'form-control'}),
    )

    parent = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput,
    )
