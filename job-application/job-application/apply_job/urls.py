from django.urls import path
from . import views

# urls for the app
urlpatterns = [
    path("", views.home_page, name="home"),
    path("home/", views.home_page, name="home"),
    path("apply/", views.application_page, name="apply"),
    path("myjobs/", views.listing_page, name="myjobs"),
    # pk should be primary key from the db
    path("edit/<str:pk>/", views.edit_form, name="edit"),
    # pk should be primary key from the db
    path("delete/<str:pk>/", views.delete_form, name="delete"),
]
