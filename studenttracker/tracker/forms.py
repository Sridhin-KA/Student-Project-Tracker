from django import forms
from .models import Batch, Student, Project


class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"