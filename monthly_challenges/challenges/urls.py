from django.urls import path
from . import views

urlpatterns = [
    #path("january", view=views.january),
    #path("february", view=views.february),
    path("<int:month>",views.monthly_challenge_by_number),
    path("<str:month>",views.monthly_challenge)
    
]
