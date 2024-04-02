from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NoticeForm
from .forms import CourseMaterialForm


def teacher_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None and user.is_active:
                login(request, user)
                return redirect('greet_teacher')
            else:
                return HttpResponse("Invalid login. Please try again.")
    else:
        form = LoginForm()
    return render(request, 'teacher/login.html', {'form': form})

def greet_teacher(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    # Change from HttpResponse to render
    return render(request, 'teacher/home.html', {'username': request.user.username})

@login_required
def teacher_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.save()
            return redirect('greet_teacher')  # Redirect or indicate success as needed
    else:
        form = NoticeForm()
    return render(request, 'teacher/teachernotice.html', {'form': form})

def add_course_material(request):
    if request.method == 'POST':
        form = CourseMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('greet_teacher')  # Corrected redirect here
    else:
        form = CourseMaterialForm()
    return render(request, 'teacher/teachercoursematerial.html', {'form': form})
