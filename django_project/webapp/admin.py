from django.contrib import admin

# Register your models here.
from .models import Employees, Users

admin.site.register(Employees)
admin.site.register(Users)