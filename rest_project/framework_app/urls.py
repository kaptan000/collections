from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'singers',views.SingerView,basename='singer'),
router.register(r'songs',views.SongView,basename='song'),

urlpatterns = [
    path('',views.startingPage.as_view(),name="starting-page"),
    path('form',views.Employee.as_view(),name='form'),
    path('detail',include(router.urls))
    # path('api-auth/', include('rest_framework.urls')),
    # path('form/<int:id>',views.Employee.as_view(),name='form'),
]
