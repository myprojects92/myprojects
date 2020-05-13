from django import forms
from django.core import validators

def starts_with_s(value):
    if value[0].lower()!='s':
        raise forms.ValidationError('the name should start with s')
    if value.isalpha() !=True:
        raise forms.ValidationError('name should contain only alphabets')

#this codes are for gmail verification
#def gmail_verification(value):
    #if value[len(value)-9:]!='gmail.com':
        #raise forms.ValidationError('email must be gmail')



class FeedBackForm(forms.Form):
    name=forms.CharField(validators=[starts_with_s])
    rollno=forms.IntegerField()
    email=forms.CharField()#(validators=[gmail_verification])
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Confirm password',widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea)#validators=[validators.MaxLengthValidator(5),validators.MinLengthValidator(2)])
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_name(self): #this clean_name is always predefined we can not cahnge it.....
        inputname=self.cleaned_data['name']
        print('validating name')
        #if len(inputname)<4:
            #raise forms.ValidationError('The length of name should be >=4')
        return inputname

    def clean_rollno(self): #this clean_rollno is always predefined we can not cahnge it.....
        inputrollno=self.cleaned_data['rollno']
        print('validating rollno')
        return inputrollno

    def clean_email(self): #this clean_email is always predefined we can not cahnge it.....
        inputemail=self.cleaned_data['email']
        print('validating email')
        return inputemail

    def clean_feedback(self): #this clean_feedback is always predefined we can not cahnge it.....
        inputfeedback=self.cleaned_data['feedback']
        print('validating feedback')
        return inputfeedback

    #total form validation in one clean method
    def clean(self):
        print('total form validation')
        cleaned_data=super().clean()
        bot_handler_value=cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError('message is from bot..... terminate it')
        inputpwd=cleaned_data['password']
        inputrpwd=cleaned_data['rpassword']
        if inputpwd !=inputrpwd:
            raise forms.ValidationError('password not matching')
        inputrollno=cleaned_data['rollno']
        if len(str(inputrollno)) !=3:
            raise forms.ValidationError('rollno must be 3 digits')
        inputname=cleaned_data['name']
        if len(inputname) <4:
            raise forms.ValidationError('name must b greater than 4')
