from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your username...',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password...'
    }))


class TeacherForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Teacher
        fields = ['username', 'password',
                  'confirm_password', 'email', 'full_name', 'address', 'image']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Passwords didnot match.")


class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['full_name', 'address', 'image']


class StudentForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Student
        fields = ['username', 'password',
                  'confirm_password', 'email', 'class_room',
                  'full_name', 'address', 'image', 'roll_no']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'class_room': forms.Select(attrs={
                'class': 'form-control'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Passwords didnot match.")


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'class_room', 'roll_no', 'address', 'image']


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['title', 'description']


class ClassRoomForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ['program', 'semester']


class AssignmnetForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['class_room',
                  'student', 'title', 'file', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }


class TeacherReviewForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['assignment_status', 'review']
