from django import forms
from .models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['course_name', 'studentname', 'teachername','genres']
    
class AddStudentForm(forms.ModelForm):
    class Meta:
        model =Music    