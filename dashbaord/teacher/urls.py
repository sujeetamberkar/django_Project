from django.urls import path
from .views import teacher_login, greet_teacher,teacher_notice, add_course_material

urlpatterns = [
    path('login/', teacher_login, name='teacher_login'),
    path('greet/', greet_teacher, name='greet_teacher'),
    path('notice/', teacher_notice, name='teacher_notice'),  # Add this line
    path('add_material/', add_course_material, name='add_course_material'),


]
