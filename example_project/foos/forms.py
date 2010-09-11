from django import forms
from models import Foo


class FooForm(forms.ModelForm):
    class Meta:
        model = Foo
