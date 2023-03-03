from django.urls import path, include

from rest_framework import routers

from .views import CarView, ReservationView, ReservationDetailView

router = routers.DefaultRouter()
router.register('car', CarView)

urlpatterns = [
    path("",include(router.urls)),
    path('reservation/', ReservationView.as_view()),
    path('reservation/<int:pk>/', ReservationDetailView.as_view())
]
