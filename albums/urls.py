from django.urls import path

from albums import views

urlpatterns = [
    path('', views.album_data, name='albums')
]
