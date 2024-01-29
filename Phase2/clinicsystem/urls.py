from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView),
    path('clinicsystem/login/', views.loginView),
    path('clinicsystem/register/', views.registerView),
    path('clinicsystem/patient_panel/', views.patientPanelView),
    path('clinicsystem/staff_panel/', views.staffPanelView),
    path('clinicsystem/appointment_active_list/', views.appointmentActiveListView),
    path('clinicsystem/appointment_history_list/', views.appointmentHistoryListView),
    path('clinicsystem/update_profile/' , views.updateprofileview),
    path('clinicsystem/appointment_reservation/' , views.appointmentreservationview)
]
