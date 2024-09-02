from django import forms

class IncomeForm(forms.Form):
    income = forms.IntegerField(max_value=None)