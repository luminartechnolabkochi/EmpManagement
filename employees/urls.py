from django.urls import path
from employees import views

urlpatterns=[
    path("add",views.add_employee,name="addemployee"),
    path("all",views.list_employees,name="listemployees"),
    path("details/<int:id>",views.employee_detail,name="empdetails"),
    path("change/<int:id>",views.employee_update,name="changeemployee"),
    path("remove/<int:id>",views.remove_employee,name="removeemployee"),
    path("accounts/signup", views.signUp, name="registration"),
    path("accounts/signin", views.signin, name="signin"),
    path("accounts/signout", views.signout, name="signout")

]