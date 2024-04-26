from django.urls import path
from . import views


urlpatterns = [
    ##path for Year_Level
    path('',views.home, name='home'),
    path('yearlevel/',views.Yearlevel),
    path('yearlevel/<int:pk>/',views.Yearlevel),

    ##path for classroom_type

    path('classtype/',views.classroomtype),
    path('classtype/<int:pk>/',views.classroomtype)

]   