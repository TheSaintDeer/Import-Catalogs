from django.urls import path

from . import views


app_name = 'detail'


urlpatterns = [
    path('<str:model_name>/', views.DetailList.as_view(), name='detail-list'),
    path('<str:model_name>/<int:pk>/', views.DetailRetrieve.as_view(), name='detail-retrieve'),
]