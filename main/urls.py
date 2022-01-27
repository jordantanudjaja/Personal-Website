from django.urls import path
from . import models, views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('favicon.png', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.png'))),
    path('', views.home, name="Home"),
    path("about/", views.about, name="About"),
    path("projects/", views.hobbies_list, {'model': models.ProjectSummary}, name="Projects"),
    path("projects/<str:project_title>/", views.project_details, name="Project Details"),
    path("cookbook/", views.hobbies_list, {'model': models.SignatureRecipe}, name="Cookbook"),
    path("cookbook/<str:recipe_name>/", views.recipe, name="Recipe"),
    path("photography/", views.hobbies_list, {'model': models.PhotoCategory}, name="Photography"),
    path("photography/<str:category>/", views.photo_details, name="Photo Details"),
    path("library/", views.hobbies_list, {'model': models.BookGenre}, name="Library"),
    path("library/<str:genre>/", views.book_reviews, name="Book Reviews"),
    path("experience/", views.experience, name="Experience"),
]
