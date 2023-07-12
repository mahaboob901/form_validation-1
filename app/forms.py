from django import forms

def valid(svalues):
    if svalues[0].islower=='a':
        raise forms.ValidationError('first letter should not be a')
    
def length(name):
    if len(name)<=5:
        raise forms.ValidationError('lenght of name is less than 5 ')

class studentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[valid,length])
    sage=forms.IntegerField()

