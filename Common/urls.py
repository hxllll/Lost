from django.conf.urls import url

from Common import views

urlpatterns = [
    url(r'^loster/', views.LosterAPIView.as_view()),
]