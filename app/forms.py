from django import forms
from django.core import validators

def validate_for_a(Svalue):
    if Svalue[0].lower()=='a':
        raise forms.ValidationError('Name should not start with a')
def validate_for_len(name):
    if len(name)<=5:
        raise forms.ValidationError('Name length should not be less than or equal to 5')
    
class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate_for_a,validate_for_len])
    sage=forms.IntegerField()
    email=forms.EmailField()
    Remail=forms.EmailField()
    url=forms.URLField()
    mobileno=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['Remail']

        if e != re:
            raise forms.ValidationError('emails are not matched')
        
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']

        if len(bot)>0:
            raise forms.ValidationError('data is not entered by human')