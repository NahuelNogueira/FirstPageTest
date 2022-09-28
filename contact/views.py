from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form=ContactForm()

    if request.method=="POST":
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            content=request.POST.get('content')

            email=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(name,email,content),
            "",["nahuel.nogueira93@gmail.com"],reply_to=[email])
            
            try:
                email.send()
                return redirect("/contact/?valid")
            except:
                redirect("/contact/?notvalid")


    return render(request, "contact/contact.html", {'my_form':contact_form})
