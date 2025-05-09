from django import forms
from .models import Member

class memberForm(forms.ModelForm):
    name=forms.CharField(label="Name",max_length=250)
    num=forms.IntegerField(label="Num")
    marks=forms.IntegerField(label="Marks")
    class Meta:
        model=Member
        fields="__all__"
