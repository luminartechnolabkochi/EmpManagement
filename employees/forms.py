from django.forms import ModelForm
from employees.models import Employees
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployeeForm(ModelForm):
    class Meta:
        model=Employees
        fields="__all__"
        exclude=("is_active",)
        widgets={
            "emp_name":forms.TextInput(attrs={"class":"form-control"}),
            "designation":forms.Select(attrs={"class":"form-select"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),

        }
        labels={
            "emp_name":"Employee_Name"
        }
    def clean(self):
        cleaned_data=super().clean()
        salary=cleaned_data["salary"]
        if salary<5000:
            msg="please enter valid salary"
            self.add_error("salary",msg)


class EmployeeSearchForm(forms.Form):
    employee_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["email","first_name","last_name","username","password1","password2"]


class SigninForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
