from django.shortcuts import render
from .models import *
from .forms import *
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, "main/home.html", {})

def about(request):
    all_skill_types = SkillType.objects.all().order_by('type')

    skill_dict = {}
    for skill_type in all_skill_types:
        skill_object = SkillType.objects.get(type = skill_type)
        tools = skill_object.tool_set.all()
        skill_dict[skill_type] = tools

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        new_form = ContactForm()

        if form.is_valid():
            name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email'] # This will validate whether its a legit email address, so things like email@nn will not work
            message = f"From: {name} ({sender_email})" + '\n\n' + form.cleaned_data['message']

            subject = "Message from Personal Website"
            recipient = ['tanudjajajordan@gmail.com']

            send_mail(subject, message, sender_email, recipient)

            jordan_message = "Thank you for your message! I'll be in touch with you as soon as possible."

            context = {
                'new_form': new_form,
                'jordan_message': jordan_message,
            }

            return render(request, 'main/About/contact message.html', context)
        else:
            jordan_message = "The email you entered is invalid. Please try again."

            context = {
                'new_form': new_form,
                'jordan_message': jordan_message,
            }

            return render(request, 'main/About/contact message.html', context)
    else: # This is when the request is a GET
        context = {
            'skill_dict': skill_dict,
            'form': form,
        }

        return render(request, "main/About/about me.html", context)

def hobbies_list(request, model): # This is a generic view that showcases the summary page of my hobbies (Projects, Cookbook, Photography, Library)
    hobby_summary = model.objects.all()

    context = {
        'hobby_summary': hobby_summary
    }

    if model.__name__.lower() == "projectsummary":
        template_name = "main/Projects/project summaries.html"
    elif model.__name__.lower() == "signaturerecipe":
        template_name = "main/Cookbook/signature recipes.html"
    elif model.__name__.lower() == "photocategory":
        template_name = "main/Photography/photo categories.html"
    elif model.__name__.lower() == "bookgenre":
        template_name = "main/Library/book genres.html"

    return render(request, template_name, context)

def project_details(request, project_title):
    project_title = project_title.replace('_', ' ')

    project_name = ProjectSummary.objects.get(title = project_title)
    project = ProjectDetail.objects.get(title = project_name) # Have to do this 2-step method because I assigned the title of Project Details to be a
                                                              # OnetoOneField from the class ProjectSummary
    background_image = project_name.project_picture.url
    title = project.title
    top_picture = project.top_picture.url
    description = project.description
    tools_used = project.tools_used
    github_link = ProjectSummary.objects.get(title = project_title).github_link
    middle_picture = project.middle_picture.url
    context = project.context
    goals = project.list_preprocessor('Goals')
    potential_improvements = project.list_preprocessor('Potential Improvements')
    bottom_picture = project.bottom_picture.url

    context = {
        'background_image': background_image,
        'title': title,
        'top_picture': top_picture,
        'description': description,
        'tools_used': tools_used,
        'github_link': github_link,
        'middle_picture': middle_picture,
        'context': context,
        'goals': goals,
        'potential_improvements': potential_improvements,
        'bottom_picture': bottom_picture,
    }

    return render(request, "main/Projects/project details.html", context)

def recipe(request, recipe_name):
    recipe_name = recipe_name.replace('_', ' ')
    dish_name = SignatureRecipe.objects.get(title = recipe_name)
    background_image = dish_name.profile_picture.url

    recipe_details = RecipeDetail.objects.filter(title = dish_name)[0]
    ingredient_dict = recipe_details.recipe_converter('Ingredients')
    preparation_dict = recipe_details.recipe_converter('Preparation')
    cooking_method_dict = recipe_details.recipe_converter('Cooking Method')

    context = {
        'recipe_name': recipe_name,
        'background_image': background_image,
        'ingredient_dict': ingredient_dict,
        'preparation_dict': preparation_dict,
        'cooking_method_dict': cooking_method_dict,
    }

    return render(request, "main/Cookbook/recipe details.html", context)

def photo_details(request, category):
    photo_category = category.replace('_', ' ')
    category_object = PhotoCategory.objects.get(title = photo_category)
    photos = category_object.photo_set.all() # Cannot use the filter method here (not sure why though), so have to use parentModel.childModel_set.all()
    background_image = category_object.profile_picture.url

    context = {
        'photo_category': photo_category,
        'background_image': background_image,
        'photos':photos,
    }

    return render(request, "main/Photography/photo details.html", context)

def book_reviews(request, genre):
    genre = genre.replace('_', ' ')
    genre_object = BookGenre.objects.get(title = genre)
    books = genre_object.book_set.all()
    background_image = genre_object.profile_picture.url

    context = {
        'genre': genre,
        'background_image': background_image,
        'books': books,
    }

    return render(request, "main/Library/book reviews.html", context)

def experience(request):
    # The experience objects are ordered in descending order of the 'end date' (Latest Experience is shown first)
    work_experience = Experience.objects.all().filter(type = "Work Experience").order_by('-end_date')
    volunteer_experience = Experience.objects.all().filter(type = "Volunteer Experience").order_by('-end_date')

    context = {
        'work_experience': work_experience,
        'volunteer_experience': volunteer_experience,
    }

    return render(request, "main/experience.html", context)
