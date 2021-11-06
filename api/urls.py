from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register('assignment', views.AssignmentViewSet)
router.register('ECE212', views.Course212ViewSet)
router.register('ECE241', views.Course241ViewSet)
router.register('ECE244', views.Course244ViewSet)
router.register('MAT290', views.Course290ViewSet)
router.register('MAT291', views.Course291ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
