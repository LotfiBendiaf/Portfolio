from django.urls import path
from .views import HomeView, facture, businessPlan, resume

urlpatterns = [
    path('', HomeView, name='Home'),
    path('facture/', facture, name='Facture'),
    path('businessPlan/', businessPlan, name='Business_Plan'),
    path('resume/', resume, name='Resume'),

]