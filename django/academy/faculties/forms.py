from django import forms
from django.forms import fields


class DepartmentAddForm(forms.Form):
    name = fields.CharField(
        label='Name:',
        max_length=100,
    )
    financing = fields.DecimalField(
        label='Financing:',
        min_value=0,
        max_digits=10,
        decimal_places=2,
    )
    building = fields.IntegerField(
        label='Building:',
        min_value=1,
        max_value=5
    )


class DepartmentDelForm(forms.Form):
    name = fields.CharField(
        label='Name:',
        max_length=100,
    )

