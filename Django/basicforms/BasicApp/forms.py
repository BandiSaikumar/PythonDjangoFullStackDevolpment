from django import forms
from django.core import validators

def check_for_s(value):
    if value[0].lower() != 's':
        raise forms.ValidationError(" Name Need To Be Starts With S")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label=" Please Enter Your Email Again! ")
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInputvalidators=[validators.MaxLengthValidators(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError(" Make Sure That Your Email Match! ")

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("INVALID ERROR")
    #     return botcatcher