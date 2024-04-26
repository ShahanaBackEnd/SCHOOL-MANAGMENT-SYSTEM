from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('yearlevel/',views.Yearlevel),
    path('yearlevel/<int:pk>/',views.Yearlevel),


]   