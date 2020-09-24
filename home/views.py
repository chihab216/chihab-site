from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    if request.method=="POST":
       
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        ins = Contact(name = name , email = email ,subject=subject , message = message )
        ins.save()

        print("tout marche")
    return render(request,'home.html')
