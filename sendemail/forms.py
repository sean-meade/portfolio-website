from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Name"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Subject"}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your e-mail"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message"})
    )