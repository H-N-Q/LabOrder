from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'devices', views.DeviceViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('add-device/', views.add_device, name='add_device'),
]
