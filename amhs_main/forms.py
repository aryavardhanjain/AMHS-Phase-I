from django import forms
from .models import Contact
from datetime import datetime, timedelta


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input-box", "placeholder": "Enter your name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "input-box", "placeholder": "Enter your email"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "input-box message-box",
                    "rows": 5,
                    "cols": 30,
                    "placeholder": "Write your message",
                }
            ),
        }
