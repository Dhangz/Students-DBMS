from django import forms 
from django.forms import ModelForm
from .models import Department, Student, Course, Enrollment, Contact


class DepartmentForm(ModelForm):
  class Meta:
    model = Department
    fields = "__all__"

class StudentForm(ModelForm):
  class Meta:
    model = Student
    fields = ('first_name', 'last_name', 'birth_date', 'department')

    widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
class CourseForm(ModelForm):
  class Meta:
    model = Course
    fields = "__all__"

class EnrollmentForm(ModelForm):
  class Meta:
    model = Enrollment
    fields = ('student', 'course', 'enrollment_date')

    widgets = {
            'enrollment_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
class ContactForm(ModelForm):
  class Meta:
    model = Contact
    fields = "__all__"