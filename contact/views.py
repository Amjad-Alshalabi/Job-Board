from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def send_message(request):

    if request.method == "POST":
        subject = request.POST['subject']
        body = {
			'name': request.POST['name'], 
			'email': request.POST['email'], 
			'message':request.POST['message'], 
			}
        message = "\n".join(body.values())
        # email = request.POST['email'] 

        send_mail(
                subject,
                message,
                'email',
                ['dr.wafiq.alshalabi@gmail.com'],
        )
    context = {}
    return render(request, 'contact/contact.html',context)


    # def log_in(request):
    #     username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     # Redirect to a success page.
    #     ...
    # else:
    #     # Return an 'invalid login' error message.
    #     ...