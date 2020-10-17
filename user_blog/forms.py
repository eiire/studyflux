from django import forms


class CommentForm(forms.Form):
    body = forms.CharField(
        label="",
        widget=forms.Textarea,
    )

    parent = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput,
    )
