from django.shortcuts import render
from django.shortcuts import redirect
from.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from django.contrib.auth import get_user_model

User = get_user_model()


@login_required(login_url='/login/')

def reciepes(request):
   if request.method == "POST":
      data = request.POST
      # print(data)

      reciepe_image = request.FILES.get('reciepe_image')
      reciepe_name = data.get('reciepe_name')
      reciepe_description = data.get('reciepe_description')

      print(reciepe_name)
      print(reciepe_description)
      print(reciepe_image)

      Reciepe.objects.create(
         reciepe_name = reciepe_name,
         reciepe_description = reciepe_description,
         reciepe_image = reciepe_image
      )
      return redirect('/reciepes/')

   queryset = Reciepe.objects.all()

   if request.GET.get('search'):
      queryset = queryset.filter(reciepe_name__icontains= request.GET.get('search') )


   context = {'reciepes':queryset}

   return render(request, 'reciepes.html',context)


# @login_required(login_url='/login/')
def update_reciepe(request,id):
   queryset = Reciepe.objects.get(id=id)

   if request.method == "POST":
      data = request.POST
      reciepe_image = request.FILES.get('reciepe_image')
      reciepe_name = data.get('reciepe_name')
      reciepe_description = data.get('reciepe_description')
      queryset.reciepe_name = reciepe_name
      queryset.reciepe_description = reciepe_description

      if reciepe_image:
         queryset.reciepe_image = reciepe_image

      queryset.save()   
      return redirect('/reciepes/')

   context = {'reciepe':queryset}
   return render(request, 'update_reciepes.html',context)


# @login_required(login_url='/login/')
def delete_reciepe(request,id):
   queryset = Reciepe.objects.get(id=id)
   queryset.delete()
   return redirect('/reciepes/')
   

def login_page(request):
   if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')

      if not User.objects.filter(username= username).exists():
         messages.error(request,'Invalid Username')
         return redirect('/login/')
      
      user = authenticate(username = username, password= password)

      if user is None:
         messages.error(request,'Invalid Password')
         return redirect('/login/')
      else:
         login(request,user)
         return redirect('/reciepes/')


   return render(request, 'login.html')
   

def logout_page(request):
   logout(request)
   return redirect('/login/')



def register_page(request):
   if request.method == "POST":
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = User.objects.filter(username=username)
      if user.exists():
         messages.info(request, "Username Already Exists")
         return redirect('/register/')


      user = User.objects.create(
         first_name = first_name,
         last_name = last_name,
         username = username,
         )
      
      user.set_password(password)
      user.save()
      messages.success(request, "Account Created Successfully")
      return redirect('/register/')


   return render(request, 'register.html')


from django.db.models import Q #for multiple seraches

def get_students(request):
   queryset = Student.objects.all()

   # ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')
   # for rank in ranks:
   #    print(rank.marks)

   if request.GET.get('search'):
      search = request.GET.get('search')
      queryset = queryset.filter(
         Q(student_name__icontains = search) |
         Q(department__department__icontains = search) |
         Q(student_id__student_id__icontains = search) |
         Q(student_email__icontains = search)
      )

   paginator = Paginator(queryset, 10)  # Show 10 contacts per page.

   page_number = request.GET.get("page", 1)
   page_obj = paginator.get_page(page_number)
   # print(page_obj)
   return render(request, 'report/students.html', {'queryset' : page_obj })


from django.db.models import Sum
from .seed import *

def see_marks(request, student_id):
   queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id )
   total_marks = queryset.aggregate(total_marks=Sum('marks'))

   return render(request, 'report/see_marks.html', {'queryset' : queryset, 'total_marks' : total_marks})