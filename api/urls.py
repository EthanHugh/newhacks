from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register('assignment', views.AssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
