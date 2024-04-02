from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import StudentLoginForm
from teacher.models import Notice  # Assuming notices are stored here
from teacher.models import CourseMaterial

def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None and user.is_active:
                login(request, user)
                return redirect('greet_student')
            else:
                return HttpResponse("Invalid login. Please try again.")
    else:
        form = StudentLoginForm()
    return render(request, 'student/login.html', {'form': form})

def greet_student(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    return render(request, 'student/home.html', {'username': request.user.username})
def student_notices(request):
    notices = Notice.objects.all().order_by('-created_at')  # Latest first
    return render(request, 'student/studentnotice.html', {'notices': notices})
def student_course_materials(request):
    materials = CourseMaterial.objects.all().order_by('-uploaded_at')
    return render(request, 'student/studentcoursematerial.html', {'course_materials': materials})
