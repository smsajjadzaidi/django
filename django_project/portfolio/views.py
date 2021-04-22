from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
# from firebase import firebase
from django.core.files import File
from django.templatetags.static import static


# Create your views here.


def index(request):
    return (render(request, 'portfolio/index.html'))


# def message(firstName, lastName, email, messageBody):
#     firebaseReq = firebase.FirebaseApplication("https://portfolio-5b10d.firebaseio.com/", None)
#
#     data = {
#         'FirstName': firstName,
#         'LastName': lastName,
#         'Email': email,
#         'Message': messageBody,
#     }
#     result = firebaseReq.post('/WebsiteUser', data)
#     print(result)
#
#
# def contact(request):
#     if request.method == 'POST':
#         firstName = request.POST['FirstName']
#         lastName = request.POST['LastName']
#         email = request.POST['Email']
#         messageBody = request.POST['messageBody']
#         message(firstName, lastName, email, messageBody)
#         return HttpResponse('Message sent successfully')
#

def blogs(request):
    return render(request, 'portfolio/blogs.html')


def blog(request):
    return render(request, 'portfolio/blog.html')




