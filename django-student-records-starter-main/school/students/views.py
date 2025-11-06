from django.shortcuts import render
# from .models import Student


from django.http import HttpResponse
from django.template import loader
from .models import Student


def students(request):
    mystudents =  Student.objects.all()
    template = loader.get_template('students/student_list.html')
    context = {
    'mystudents': mystudents,
  }
    return HttpResponse(template.render(context, request))
    
# def students(request):
    # return HttpResponse("Hello world!")

# TODO: Create a view function to display all students.
# Use Student.objects.all() to fetch data.
# Pass it into a template (student_list.html).
