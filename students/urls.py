
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudSelectionViewSet

router = DefaultRouter()
router.register(r'students', StudSelectionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]