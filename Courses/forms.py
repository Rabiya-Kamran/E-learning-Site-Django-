from django import forms
from .models import Course  # Replace with the actual name of your model

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course  # Specify the model to use
        fields = ['title', 'description']  # Replace with the fields in your model
