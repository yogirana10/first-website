# Prashant_Resume/urls.py
from django.conf.urls import url
from Prashant_Resume import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]