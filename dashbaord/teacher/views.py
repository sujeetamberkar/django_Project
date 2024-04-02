from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NoticeForm
from .forms import CourseMaterialForm
from .models import StudentMarks
from .forms import MarksForm
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect

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
@login_required
def enter_marks(request):
    if request.method == 'POST':
        # This part needs to be adapted based on your form submission logic.
        pass
    else:
        students = User.objects.all()  # Adjust this based on how you track students
        marks = StudentMarks.objects.all()
        return render(request, 'teacher/teachermarks.html', {'students': students, 'marks': marks})

@login_required
def update_marks(request):
    if request.method == 'POST':
        # Process the form submission
        for key, value in request.POST.items():
            if key.startswith('marks_obtained_'):
                student_id = key.split('_')[-1]
                marks_obtained = request.POST.get(f'marks_obtained_{student_id}')
                total_marks = request.POST.get(f'total_marks_{student_id}')
                
                # Update the StudentMarks model
                student = User.objects.get(id=student_id)
                StudentMarks.objects.update_or_create(
                    student=student,
                    defaults={
                        'marks_obtained': marks_obtained,
                        'total_marks': total_marks
                    }
                )
        return redirect('teacher_enter_marks')  # Redirect back to the marks entry page or another appropriate page
    else:
        # Handle the case for GET request or redirect as necessary
        return redirect('teacher_enter_marks')
