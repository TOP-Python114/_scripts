from django import forms
from django.forms import fields
from django.forms import widgets


class DepartmentAddForm(forms.Form):
    name = fields.CharField(
        label='Name:',
        max_length=100,
        widget=widgets.TextInput(
            attrs={
                'placeholder': ''
            }
        ),
    )
    financing = fields.DecimalField(
        label='Financing:',
        min_value=0,
        max_digits=10,
        decimal_places=2,
        widget=widgets.NumberInput(
            attrs={
                'placeholder': ''
            }
        ),
    )
    building = fields.IntegerField(
        label='Building:',
        min_value=1,
        max_value=5,
        widget=widgets.NumberInput(
            attrs={
                'placeholder': ''
            }
        ),
    )


class DepartmentDelForm(forms.Form):
    name = fields.CharField(
        label='Name:',
        max_length=100,
        widget=widgets.TextInput(
            attrs={
                'placeholder': ''
            }
        )
    )

