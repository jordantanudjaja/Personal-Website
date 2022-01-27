from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .. import views, models

# This test file checks whether the urls in urls.py are directing towards the specified functions in views.py

class TestUrls(SimpleTestCase):
    def test_home(self):
        url_path = reverse("Home")
        self.assertEqual(resolve(url_path).func, views.home)

    def test_about(self):
        url_path = reverse("About")
        self.assertEqual(resolve(url_path).func, views.about)

    def test_projects(self):
        url_path = reverse("Projects")
        self.assertEqual(resolve(url_path).func, views.hobbies_list)
        self.assertEqual(resolve(url_path).kwargs, {'model': models.ProjectSummary})

    def test_project_details(self):
        url_path = reverse("Project Details", args=['some_project_title'])
        self.assertEqual(resolve(url_path).func, views.project_details)

    def test_cookbook(self):
        url_path = reverse("Cookbook")
        self.assertEqual(resolve(url_path).func, views.hobbies_list)
        self.assertEqual(resolve(url_path).kwargs, {'model': models.SignatureRecipe})

    def test_recipe(self):
        url_path = reverse("Recipe", args=['some_recipe_name'])
        self.assertEqual(resolve(url_path).func, views.recipe)

    def test_photography(self):
        url_path = reverse("Photography")
        self.assertEqual(resolve(url_path).func, views.hobbies_list)
        self.assertEqual(resolve(url_path).kwargs, {'model': models.PhotoCategory})

    def test_photo_details(self):
        url_path = reverse("Photo Details", args=['some_photo_category'])
        self.assertEqual(resolve(url_path).func, views.photo_details)

    def test_library(self):
        url_path = reverse("Library")
        self.assertEqual(resolve(url_path).func, views.hobbies_list)
        self.assertEqual(resolve(url_path).kwargs, {'model': models.BookGenre})

    def test_book_reviews(self):
        url_path = reverse("Book Reviews", args=['some_book_genre'])
        self.assertEqual(resolve(url_path).func, views.book_reviews)

    def test_experience(self):
        url_path = reverse("Experience")
        self.assertEqual(resolve(url_path).func, views.experience)
