from django.test import TestCase, Client
from django.urls import reverse
from ..models import *
import tempfile

# This test file tests whether the views in views.py is directing towards the correct html templates,
# whether those templates are being rendered correctly, and whether the correct dictionaries (context)
# are passed to those templates. This test file does not test whether the models output data correctly
# in a readable format in the view, but rather mocks the models required to test whether the views are
# successfully rendered.

# The response status code == 200 is a general test to show the view function is being rendered correctly in the browser.
# The template used assertion tests whether the correct html template is being rendered in each view.
# The assertIn function tests whether the corect context is being passed through each template in the view.

# Any models that are mocked in the test files are immediately deleted after executing the tests.

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        # Creating a Mock ProjectSummary Object
        ProjectSummary.objects.create(
            title = "Project Summary 1",
            project_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name, # Mocking the ImageField
            summary = "summary",
            github_link = "github link",
            additional_links = ""
        )

        # Creating a Mock ProjectDetail Object
        ProjectDetail.objects.create(
            title = ProjectSummary.objects.get(title = "Project Summary 1"),
            top_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            description = "description",
            tools_used ="tools used",
            middle_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            context = "context",
            goals = "goals",
            potential_improvements = "potential improvements",
            bottom_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

        # Creating a Mock SignatureRecipe Object
        SignatureRecipe.objects.create(
            title = "Signature Recipe 1",
            profile_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

        # Creating a Mock RecipeDetail Object
        RecipeDetail.objects.create(
            title = SignatureRecipe.objects.get(title = "Signature Recipe 1"),
            ingredients = "ingredients",
            preparation = "preparation",
            cooking_method = "cooking method"
        )

        # Creating a mock PhotoCategory Object
        PhotoCategory.objects.create(
            title = "Photo Category 1",
            profile_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

        # Creating a mock Photo Object
        Photo.objects.create(
            picture = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_category = PhotoCategory.objects.get(title = "Photo Category 1"),
            title = "title"
        )

        # Creating a mock BookGenre Object
        BookGenre.objects.create(
            title = "Book Genre 1",
            profile_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

        # Creating a mock Book Object
        Book.objects.create(
            book_genre = BookGenre.objects.get(title = "Book Genre 1"),
            title = "title",
            author = "author",
            picture = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            book_review = "book review"
        )

    def test_home_GET(self):
        home_url = reverse('Home')
        response = self.client.get(home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/home.html")

    def test_about_GET(self):
        about_url = reverse('About')
        response = self.client.get(about_url)

        context_content = {
            'skill_dict',
            'form',
        }

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/About/about me.html")
        self.assertTrue(context_content.issubset(response.context.keys())) # Testing whether the context that is passed has the above-mentioned keys

    def test_about_POST(self):
        about_url = reverse('About')
        response = self.client.post(about_url)

        context_content = {
            'new_form',
            'jordan_message',
        }

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/About/contact message.html")
        self.assertTrue(context_content.issubset(response.context.keys())) # Testing whether the context that is passed has the above-mentioned keys

    def test_project_summaries_GET(self):
        projects_url = reverse("Projects")
        response = self.client.get(projects_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/Projects/project summaries.html")
        self.assertIn('hobby_summary', response.context.keys()) # Testing whether hobby_summary is in the context passed
        self.assertIsInstance(response.context['hobby_summary'][0], ProjectSummary) # Testing whether the list of elements in hobby_summary is of class ProjectSummary

    def test_project_details_GET(self):
        project_details_url = reverse("Project Details", args=['Project_Summary_1'])
        response = self.client.get(project_details_url)

        context_content = {
            'background_image',
            'title',
            'top_picture',
            'description',
            'tools_used',
            'github_link',
            'middle_picture',
            'context',
            'goals',
            'potential_improvements',
            'bottom_picture',
        }

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/Projects/project details.html")
        self.assertTrue(context_content.issubset(response.context.keys())) # Testing whether the context that is passed has the above-mentioned keys

    def test_signature_recipes_GET(self):
        cookbook_url = reverse("Cookbook")
        response = self.client.get(cookbook_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/Cookbook/signature recipes.html")
        self.assertIn('hobby_summary', response.context.keys()) # Testing whether hobby_summary is in the context passed
        self.assertIsInstance(response.context['hobby_summary'][0], SignatureRecipe) # Testing whether the list of elements in hobby_summary is of class SignatureRecipe

    def test_recipe_GET(self):
        recipe_url = reverse("Recipe", args=['Signature_Recipe_1'])
        response = self.client.get(recipe_url)

        context_content = {
            'recipe_name',
            'background_image',
            'ingredient_dict',
            'preparation_dict',
            'cooking_method_dict',
        }

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/Cookbook/recipe details.html")
        self.assertTrue(context_content.issubset(response.context.keys())) # Testing whether the context that is passed has the above-mentioned keys

    def test_photo_categories_GET(self):
        photography_url = reverse("Photography")
        response = self.client.get(photography_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/Photography/photo categories.html")
        self.assertIn('hobby_summary', response.context.keys()) # Testing whether hobby_summary is in the context passed
        self.assertIsInstance(response.context['hobby_summary'][0], PhotoCategory) # Testing whether the list of elements in hobby_summary is of class PhotoCategory

    def test_photo_details_GET(self):
        photo_details_url = reverse("Photo Details", args=['Photo_Category_1'])
        response = self.client.get(photo_details_url)

        context_content = {
            'photo_category',
            'background_image',
            'photos',
        }

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/Photography/photo details.html")
        self.assertTrue(context_content.issubset(response.context.keys())) # Testing whether the context that is passed has the above-mentioned keys

    def test_book_genres_GET(self):
        library_url = reverse("Library")
        response = self.client.get(library_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/Library/book genres.html")
        self.assertIn('hobby_summary', response.context.keys()) # Testing whether hobby_summary is in the context passed
        self.assertIsInstance(response.context['hobby_summary'][0], BookGenre) # Testing whether the list of elements in hobby_summary is of class BookGenre

    def test_book_reviews_GET(self):
        book_reviews_url = reverse("Book Reviews", args=['Book_Genre_1'])
        response = self.client.get(book_reviews_url)

        context_content = {
            'genre',
            'background_image',
            'books',
        }

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/Library/book reviews.html")
        self.assertTrue(context_content.issubset(response.context.keys())) # Testing whether the context that is passed has the above-mentioned keys

    def test_experience_GET(self):
        experience_url = reverse("Experience")
        response = self.client.get(experience_url)

        context_content = {
            'work_experience',
            'volunteer_experience',
        }

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/experience.html")
        self.assertTrue(context_content.issubset(response.context.keys())) # Testing whether the context that is passed has the above-mentioned keys
