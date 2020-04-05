from .forms import ContactForm
from .models import Contact
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here. 
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            contact_=Contact(name=name,email=email,message=message)
            contact_.save()
            return redirect('/user/mainPage')
    else:
        form=ContactForm()
    context={'form':form}
    return render(request,"Contact.html",context)