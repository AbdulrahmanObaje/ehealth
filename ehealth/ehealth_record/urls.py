from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("dashboard", views.dashboard, name= "dashboard"),

    path("post_record", views.post_record_request, name= "post_record"),
    path("post_appointment", views.book_appointment_request, name= "post_appointment"),
    path("view_patient", views.view_patient_request, name= "view_patient"),
    path("view_record", views.view_record_request, name= "view_record"),
    path("view_statistics", views.view_statistics_request, name= "view_statistics"),
    path("my_appointments", views.view_request_my_appointments, name= "my_appointments"),
    path("appointmentconfirm/<int:id>/<str:confvalue>/", views.view_Appointment_Confirms, name= "appointmentconfirm"),

    path("dopostrecord", views.do_post_record, name= "dopostrecord"),
    path("dopostappointment", views.do_book_appointment, name= "dopostappointment"),
    path("get_user_appointment/", views.getPatientAppointment, name="get_user_appointment"),
    path("get_patients_by_ailment", views.getPatientByAilment, name="get_patients_by_ailment"),
    path("get_physician_by_name", views.getPhysicianByName, name="get_physician_by_name"),
    
    path("patient/<int:id>/", views.patient_request, name="patient"),
]