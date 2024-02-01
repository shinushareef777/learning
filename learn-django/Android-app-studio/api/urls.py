from django.urls import path
from .views import AndroidAppDetailApiView,  AndroidAppListCreateApiView, AndroidAppUpdateApiView, AndroidAppDestroyApiView

urlpatterns = [
    path("<int:pk>/", AndroidAppDetailApiView.as_view()),
    path("", AndroidAppListCreateApiView.as_view()),
    path("<int:pk>/update", AndroidAppUpdateApiView.as_view()),
    path("<int:pk>/delete", AndroidAppDestroyApiView.as_view()),
  ]
