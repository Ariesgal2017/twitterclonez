from django import forms

class TweetForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)

