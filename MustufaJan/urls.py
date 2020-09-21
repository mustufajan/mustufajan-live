from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path("", views.profile, name="profile"),
    path("skills", views.skills, name="skills"),
]