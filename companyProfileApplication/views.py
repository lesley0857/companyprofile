from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# Create your views here.

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def index_view(request):
    return render(request,'index.html')

def projects(request):
    return render(request,'projects.html')

def projects_details(request,id):
    return render(request,'projects-details.html')

def quote_view(request):
    if request.method == 'POST':
        user= request.POST.get('name')
        html_content = render_to_string(
            ['order_templates/orderCreated.html'],{"user":user})
        subject= 'Order Created'
        from_email= 'nwekelesley@gmail.com'
        to=request.POST.get('email')
        message = EmailMessage(subject=subject,
                            body=html_content,
                            from_email=from_email,
                            to=[to],)
        message.content_subtype = 'html'
        message.send()
        return HttpResponse(html_content)
    
def services(request):
    return render(request,'services.html')

def services_details(request,id):
    return render(request,'services-details.html')