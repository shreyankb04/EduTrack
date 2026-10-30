from django.urls import path
from . import views

urlpatterns = [

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Student Management
    path('add/', views.add_student, name='add_student'),

    path('edit/<int:student_id>/',
         views.edit_student,
         name='edit_student'),

    path('delete/<int:student_id>/',
         views.delete_student,
         name='delete_student'),

    # Course Management
    path('courses/',
         views.course_list,
         name='course_list'),

    path('courses/add/',
         views.add_course,
         name='add_course'),

]