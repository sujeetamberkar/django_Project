from django.urls import path
from .views import student_login, greet_student,student_notices,student_course_materials

urlpatterns = [
    path('login/', student_login, name='student_login'),
    path('home/', greet_student, name='greet_student'),
    path('notices/', student_notices, name='student_notices'),  # Add this line
    path('course_materials/', student_course_materials, name='student_course_materials'),


]
