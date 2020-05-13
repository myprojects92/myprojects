from django.shortcuts import render
from . import forms
# Create your views here.

def feedback_view(request):
    if request.method=='GET':
        form = forms.FeedBackForm()

    if request.method=='POST':    # it means if it contains some data
        form=forms.FeedBackForm(request.POST)    # it means if the request is POST then can u please create a form object i.e whatever data is there inside form can u plz again create a form object
        if form.is_valid():
            print('form validation completed and printing feedback information')
            print('student name:',form.cleaned_data['name'])  # cleaned  means already validated data
            print('student rollno:',form.cleaned_data['rollno'])
            print('student email id:',form.cleaned_data['email'])
            print('student feedback:', form.cleaned_data['feedback']) #whenever we submit the form then only this code i.e from if request.method=='POST': ......to print (..) will execute
            return render(request,'testapp/thankyou.html',{'name':form.cleaned_data['name']})
    return render(request,'testapp/feedback.html',{'form':form})
