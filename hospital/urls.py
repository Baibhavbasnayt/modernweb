from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('department/', views.department, name="department"),
    path('doctor/', views.doctor, name="doctor"),
    path('about/', views.show_about, name="about"),
    path('contact/', views.show_contact, name="contact"),

    path('staradmin/', views.admin, name="staradmin"),
    path('admindash/', views.admin_dashboard, name="admindash"),
    path('login/', views.login, name="login"),

    path('adminlogin/', views.admin_login, name="adminlogin"),
    path('adminsignup/', views.admin_signup, name="adminsignup"),

    path('doctoradd/', views.add_doctor, name="doctoradd"),
    path('showdoctor/', views.show_doctor, name="showdoctor"),
    path('updatedoctor/<int:id>/', views.update_doctor,name='updatedoctor'),
    path('deletedoctor/<int:id>/', views.delete_doctor,name='deletedoctor'),

    path('departmentadd/', views.add_department, name="departmentadd"),
    path('showdepartment/', views.show_department, name="showdepartment"),
    path('updatedepartment/<int:id>/', views.update_department, name='updatedepartment'),
    path('deletedepartment/<int:id>/', views.delete_department, name='deletedepartment'),

    path('appointmentadd/', views.add_appointment, name="appointmentadd"),
    path('showappointment/', views.show_appointment, name="showappointment"),
    path('updateappointment/<int:id>/', views.update_appointment, name='updateappointment'),
    path('deleteappointment/<int:id>/', views.delete_appointment, name='deleteappointment'),
    ]

