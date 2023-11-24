from django.urls import path
from . import views

urlpatterns = [
    path('',views.startingPage.as_view(),name="starting-page"),
    path('form',views.Employee.as_view(),name='form'),
    # path('form/<int:id>',views.Employee.as_view(),name='form'),
]
