from django import forms
from django.forms import DateInput, DateField
from django.contrib.admin.widgets import AdminDateWidget
from .models import kesif



class KesifForm(forms.ModelForm):
    tarih = DateField(widget=AdminDateWidget)
    class Meta:
        model=kesif
        fields=[
            'kesifNo',
            'tarih',
            'musteri',
            'ilgiliKisi',
            'tel',
            'adres',
            'aciklama',
        ]
    widgets = {
             'tarih': DateInput(attrs={'type': 'date'})
        }

