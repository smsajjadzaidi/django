from django.db import models


class Employees(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    employee_id = models.IntegerField(null=True)

    def __str__(self):
        return self.first_name


class Users(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email

