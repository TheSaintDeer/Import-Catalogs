from django.urls import path, re_path

from . import views


app_name = 'importing'


urlpatterns = [
    path('import/', views.Importing.as_view()),
    path('detail/<str:model_name>/', views.DetailList.as_view()),
    path('detail/<str:model_name>/<int:pk>/', views.DetailRetrieve.as_view()),
]