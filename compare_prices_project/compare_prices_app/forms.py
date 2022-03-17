from dataclasses import field
from django import forms


class CompareForm(forms.Form):
    name = forms.CharField(
        label='検索',
        max_length=50,
    )

