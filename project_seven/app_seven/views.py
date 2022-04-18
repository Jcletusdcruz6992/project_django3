from django.shortcuts import render

# Create your views here.
from app_seven import forms
from app_seven.forms import NewUser
def index(request):
    return render(request,'app_seven\index.html')

def form_page(request):
    form=NewUser()

    if request.method=="POST":
        form=NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Validation Success !')
            print('NAME:'+ form.cleaned_data['name'])
            print('EMAIL:'+ form.cleaned_data['email'])
        else:
            print("Error in Form")

    return render(request,'app_seven/form_page.html',{'form':form})
