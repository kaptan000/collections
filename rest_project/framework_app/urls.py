from django.urls import path
from . import views

urlpatterns = [
    path('',views.startingPage.as_view(),name="starting-page"),
    path('form',views.employee.as_view(),name='form'),
    path('form/<int:id>',views.employee.as_view(),name='form'),
]
