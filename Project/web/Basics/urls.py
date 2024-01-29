from django.urls import path,include
from Basics import views

urlpatterns = [
    path('Calculator/',views.Calculator),
    path('Largest/',views.Largest),
    path('Marksheet/',views.Marksheet),
    path('BasicSalary/',views.BasicSalary),
]