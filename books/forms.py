from django import forms


class AuthorForm(forms.Form):
    first_name = forms.CharField(label="first_name", max_length=32)
    last_name = forms.CharField(label="last_name", max_length=32)


class BookForm(forms.Form):
    title = forms.CharField(label="title", max_length=128)
    date = forms.DateField()
    author_id = forms.IntegerField()
