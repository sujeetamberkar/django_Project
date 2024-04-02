from django import forms
from .models import Notice
from .models import CourseMaterial
from .models import StudentMarks

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
class CourseMaterialForm(forms.ModelForm):
    class Meta:
        model = CourseMaterial
        fields = ['chapter_name', 'notes', 'video_url']
class MarksForm(forms.ModelForm):
    class Meta:
        model = StudentMarks
        fields = ['student', 'marks_obtained', 'total_marks']
