from django import forms

from purchase.models import UserCheckout


class OrderUser(forms.ModelForm):
    class Meta:
        model = UserCheckout
        exclude = ('user', 'address')
