from django.shortcuts import render
from website.models import Contact

# Create your views here.
def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        course = request.POST['course']
        remark = request.POST['remark']
        data = Contact(name=name, contact=contact, email=email, course=course)
        data.save()
    return render(request, 'website/contact.html')
