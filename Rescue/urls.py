from django.conf.urls import url

from Rescue import views

urlpatterns = [
    url(r'^users/', views.RescueUsersAPIView.as_view()),

]