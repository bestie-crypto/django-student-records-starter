from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
     path('students/', views.students, name='students'),
    # TODO: Add path for the student list view
]
