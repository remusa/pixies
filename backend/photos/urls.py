from django.urls import path

from .views import PhotosListView


urlpatterns = [path("", PhotosListView.as_view())]
