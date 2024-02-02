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
    path('clinicsystem/appointment/<int:appointmentId>/', views.appointmentView),
    path('clinicsystem/appointment/<int:appointmentId>/cancel/', views.cancelAppointmentView),
    path('clinicsystem/clinic_list/', views.clinicListView),
    path('clinicsystem/payment_list/', views.paymentListView),
    path('clinicsystem/reserve/', views.reserveView),
    path('clinicsystem/appointment_list/', views.appointmentListView),
    path('clinicsystem/service_list/', views.serviceListView),
    path('clinicsystem/notification_list/', views.notificationListView),
    path('clinicsystem/create_clinic/', views.createClinicView),
    path('clinicsystem/create_service/', views.createServiceView),
    path('clinicsystem/create_payment/', views.createPaymentView),
    path('clinicsystem/clinic/<int:clinicId>/', views.clinicView),
    path('clinicsystem/service/<int:serviceId>/', views.serviceView),
    path('clinicsystem/payment/<int:paymentId>/', views.paymentView),
    path('clinicsystem/clinic_list1/', views.clinicList1View),
    path('clinicsystem/payment_list1/', views.paymentList1View),
    path('clinicsystem/service_list1/', views.serviceList1View),
]
