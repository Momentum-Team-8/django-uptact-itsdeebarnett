from django.forms import ModelForm, Textarea
from django.db import models
from django.db.models import fields
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        widgets = {"note": Textarea(attrs={"cols":80, "rows":20})}
        model = Contact
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
        ]

# class NoteForm(ModelForm):
#     class Meta:
#         model = Note
#         fields = ['note',]