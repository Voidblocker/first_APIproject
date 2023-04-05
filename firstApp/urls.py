from django.urls import path
from .views import StudentList,StudentDetails,GraduatingStudents

urlpatterns = [
    path('students/', StudentList.as_view() , name ='student_list'),
    path('students_list', GraduatingStudents.as_view() , name='studentlist'),
    path('students/<int:pk>', StudentDetails.as_view(), name='student_detail')
]