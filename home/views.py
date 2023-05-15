from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
#     return HttpResponse("Hey I'm a Django Server")
      peoples = [
           {'name':'Abhijeet','age':26},
           {'name':'Ram','age':24},
           {'name':'Raju','age':22},
           {'name':'Abhi','age':14},
           {'name':'Jeet','age':18},
           {'name':'Sandeep','age':30},
      ]

      text = """
      Create a Django app: Django projects are made up of multiple apps. Each app has its own models, views, and templates. To create a new app, navigate to your project directory and type python manage.py startapp appname.
      """

      vegetables = ['pumpkin','tomato','potato']
      return render(request,"index.html",context={'page':'Django ','peoples':peoples,'text':text,'vegetables':vegetables})



def about(request):
    context = {'page':'about'}
    return render(request,"about.html",context)




def contact(request):
    context = {'page':'contact'}
    return render(request,"contact.html",context)


def success_page(request):
#     print("*"*10)
    return HttpResponse("Hey I'm a success page")