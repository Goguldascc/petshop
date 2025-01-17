from django import forms
from. models import reg_tbl
from django.forms import TextInput,EmailInput
class regform(forms.ModelForm):
    class Meta:
        model =reg_tbl
        fields=['fn','mb','em','ps','cps']
                                                  
        