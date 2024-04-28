# urls.py in the students app

from django.urls import path
from students import views

urlpatterns = [
    path('student/getAll', views.get_all_students, name='get_all_students'),
    path('student/addFromCSV', views.add_students_from_csv, name='add_from_csv'),
    path('student/deleteAll', views.delete_all_students, name='delete_all_students'),
]
