from django.urls import path,include
from rest_api import views
from rest_api.views import BhojanViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('bhojan',BhojanViewset,basename = 'bhojan')


urlpatterns = [
    path('bhojan_list/',views.bhojan_list),
    path('bhojan_list/<int:id>/',views.bhojan_details),
    path('viewset/<int:pk>/',include(router.urls)),
    ]