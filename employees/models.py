from django.db import models

# Create your models here.


class Employees(models.Model):
    emp_name=models.CharField(max_length=120)
    options=(("ceo","ceo"),
             ("admin","admin"),
             ("hr","hr"),
             ("telecaller","telecaller"),
             ("faculty","faculty"),
             ("seo","seo"))
    designation=models.CharField(max_length=120,choices=options,null=True,default="hr")
    salary=models.PositiveIntegerField()
    address=models.CharField(max_length=120)
    email=models.CharField(max_length=120,unique=True)
    phone=models.CharField(max_length=15,unique=True)
    is_active=models.BooleanField(default=True,null=True)

    def __str__(self):
        return self.emp_name