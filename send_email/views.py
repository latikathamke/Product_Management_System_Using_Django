from django.shortcuts import render
from django.core.mail import send_mail
from product_management.settings import EMAIL_HOST_USER

# Create your views here.
subject = 'This is the subject of my mail hello everybody'
message='This is the test message body from django product management website'
receiver=['to@gmail.com']
def send_my_mail(request):
    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        receiver, 
        fail_silently=False
    )

    return render(request, 'sendMail/sendMail.html')