from django import forms
from .models import Student, Course


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'name',
            'email',
            'phone',
            'course'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter student name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),

            'course': forms.Select(attrs={
                'class': 'form-select'
            })
        }