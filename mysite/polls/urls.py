from django.urls import path

from . import views

# To map the views to URLs.
urlpatterns = [
    path('', views.index, name='index')
]