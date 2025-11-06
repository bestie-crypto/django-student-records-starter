from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email","Department","datecreated",)
    
# Register your models here.
admin.site.register(Student,StudentAdmin)


