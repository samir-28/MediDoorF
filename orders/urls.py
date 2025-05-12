from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.payments, name='payments'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_complete/', views.order_complete, name='order_complete'),
    path('subscription/', views.subscription, name='subscription'),
    path('prescribtion/', views.prescribtion, name='prescribtion'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('prescribtion_enquiry/', views.prescribtion_enquiry, name='prescribtion_enquiry')
]
