from django.shortcuts import render,redirect
from employees import forms
from employees.models import Employees
from django.contrib.auth import authenticate,login,logout
from employees.decorators import signin_required
# Create your views here.

@signin_required
def add_employee(request,*args,**kwargs):

    form=forms.EmployeeForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            print("employee has been added")
            return redirect("listemployees")
        else:
            context={"form":form}
            return render(request, "add_emp.html", context)

    return render(request,"add_emp.html",context)

@signin_required
def list_employees(request,*args,**kwargs):

    employees=Employees.objects.filter(is_active=True)
    form=forms.EmployeeSearchForm()
    context={"employees":employees,"form":form}
    if request.method=="POST":
        form=forms.EmployeeSearchForm(request.POST)
        if form.is_valid():
            ename=form.cleaned_data["employee_name"]
            employees=Employees.objects.filter(emp_name__contains=ename)
            form=forms.EmployeeSearchForm()
            context={"employees":employees,"form":form}
            return render(request, "list_emp.html", context)

    return render(request,"list_emp.html",context)
@signin_required
def employee_detail(request,*args,**kwargs):
    id=kwargs["id"]
    employee=Employees.objects.get(id=id)
    context={"employee":employee}
    return render(request,"detail_emp.html",context)

@signin_required
def employee_update(request,*args,**kwargs):
    id=kwargs["id"]
    employee=Employees.objects.get(id=id)
    form=forms.EmployeeForm(instance=employee)
    context={"form":form}
    if request.method=="POST":
        form=forms.EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect("listemployees")
        else:
            context={"form":form}
            return render(request, "change_emp.html", context)

    return render(request,"change_emp.html",context)

@signin_required
def remove_employee(request,*args,**kwargs):
    id=kwargs["id"]
    employee=Employees.objects.get(id=id)
    employee.is_active=False
    employee.save()
    return redirect("listemployees")


def signUp(request):
    form=forms.UserRegistrationForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            context={"form":form}
            return render(request, "register.html", context)

    return render(request,"register.html",context)

def signin(request):
    form=forms.SigninForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.SigninForm(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data["username"]
            pwd=form.cleaned_data["password"]
            user=authenticate(request,username=user_name,password=pwd)
            if user:
                login(request,user)
                return redirect("listemployees")
            else:
                context={"form":form}
                return render(request, "login.html", context)

    return render(request,"login.html",context)

@signin_required
def signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")