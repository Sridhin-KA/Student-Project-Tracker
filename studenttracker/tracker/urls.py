from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('batch/<int:id>/', views.batch_detail, name='batch_detail'),

    path(
        'student/<int:id>/',
        views.student_detail,
        name='student_detail'
    ),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path(
        'batch/add/',
        views.add_batch,
        name='add_batch'
    ),

    path(
        'student/add/',
        views.add_student,
        name='add_student'
    ),

    path(
        'batch/delete/<int:id>/',
        views.delete_batch,
        name='delete_batch'
    ),

    path(
        'student/delete/<int:id>/',
        views.delete_student,
        name='delete_student'
    ),path(
    "batch/edit/<int:id>/",
    views.edit_batch,
    name="edit_batch",
),

path(
    "student/edit/<int:id>/",
    views.edit_student,
    name="edit_student",
),
path(
    "project/add/",
    views.add_project,
    name="add_project",
),
path( "projects/manage/", views.manage_projects, name="manage_projects", ),

path(
    "project/edit/<int:id>/",
    views.edit_project,
    name="edit_project",
),

path(
    "project/delete/<int:id>/",
    views.delete_project,
    name="delete_project",
),


]