from . import views
from django.contrib import admin
from django.urls import include, path

app_name = "survey"
urlpatterns = [
    path("", views.index, name="survey_home"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]