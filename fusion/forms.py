from django import forms


class FusionForm(forms.Form):
    CHOICES = (('1', 'Apple'), ('2', 'Pinapple'))
    fruit = forms.ChoiceField(label="Fruit", required=True, widget=forms.RadioSelect, choices=CHOICES)
    has_pen = forms.BooleanField(label="Pen", required=True, widget=forms.CheckboxInput)
