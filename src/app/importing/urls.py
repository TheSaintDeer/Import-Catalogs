from django.urls import path

from . import views


app_name = 'importing'


urlpatterns = [
    path('', views.Importing.as_view()),
]