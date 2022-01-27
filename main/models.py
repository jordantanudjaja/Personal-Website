from django.db import models

# Create your models here.

class SkillType(models.Model):
    class Meta:
        verbose_name_plural = "Skill Types"

    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type

class Tool(models.Model):
    name = models.CharField(max_length=200)
    skill_type = models.ForeignKey(SkillType, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="images/About/")

    def __str__(self):
        return self.name

class ProjectSummary(models.Model):
    class Meta:
        verbose_name_plural = "Project Summaries"

    title = models.CharField(max_length=200)
    project_picture = models.ImageField(upload_to='images/Projects/Project Summary/')
    summary = models.TextField(default="")
    github_link = models.CharField(max_length=200)
    additional_links = models.TextField(default="", null=True, blank=True, verbose_name="Additional Links (Format: 'Alias': 'url'):")

    def __str__(self):
        return self.title

    def hyperlink(self):
        """
        Converts the title to an acceptable hyperlink format and returns that format
        """
        return self.title.replace(' ', '_')

    def link_converter(self):
        """
        A Method that converts each project's Additional Links section input to a readable output in the form of an ordered list,
        hiding the long url of the additional links in an alias, and returning a dictionary containing the key-value pair as
        'Alias': 'url' if user did input additioanl links, otherwise it returns an empty space.
        """
        if self.additional_links != "":
            ordered_list = self.additional_links.split('\r\n')
            link_dict = {}
            for pair in ordered_list:
                list_ = pair.split(': ')
                link_dict[list_[0]] = list_[1]

            return link_dict
        else:
            return ""

class ProjectDetail(models.Model):
    class Meta:
        verbose_name_plural = "Project Details"

    title = models.OneToOneField(ProjectSummary, on_delete=models.CASCADE)

    top_picture = models.ImageField(upload_to='images/Projects/Project Detail/')
    description = models.TextField(default="")
    tools_used = models.TextField(default="")

    middle_picture = models.ImageField(upload_to='images/Projects/Project Detail/')

    context = models.TextField(default="")
    goals = models.TextField(default="", verbose_name="Goals (Format: 1), 2)):")
    potential_improvements = models.TextField(default="", verbose_name="Potential Improvements (Format: 1), 2))")

    bottom_picture = models.ImageField(upload_to='images/Projects/Project Detail/')

    def __str__(self):
        return self.title.title

    def list_preprocessor(self, section):
        """
        A Method that converts each project's section that contains an ordered list (Goals, Potential Improvements) input to
        a readable output that the user can see in the view, and returns a list with unecessary bullet points removed, and only
        contains the essential content of that section

        Parameters:
        -----------
        section: str
            Values can only be from {'Goals', 'Potential Improvements'}
        """
        # Code block to split the content of each section into a list containing each sentence as the elements
        if section.lower() == "goals":
            ordered_list = self.goals.split('\r\n')
        else:
            ordered_list = self.potential_improvements.split('\r\n')

        # Code block to remove the unnecessary ordered list bullets (e.g: 1), 2), 3)) from each sentence
        for i in range(len(ordered_list)):
            ordered_list[i] = ordered_list[i][3:] # This only works if the input is in the form 1) Loren ipsum, and not 1)Loren ipsum
            if ordered_list[i][0] == " ": # This captures ordered list items more than 9) until 99)
                ordered_list[i] = ordered_list[i][1:]

        return ordered_list

class SignatureRecipe(models.Model):
    class Meta:
        verbose_name_plural = "Signature Recipes"

    title = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to="images/Cookbook/")

    def __str__(self):
        return self.title

    def hyperlink(self):
        """
        Converts the title to an acceptable hyperlink format and returns that format
        """
        return self.title.replace(' ', '_')

class RecipeDetail(models.Model):
    class Meta:
        verbose_name_plural = "Recipe Details"

    title = models.OneToOneField(SignatureRecipe, on_delete=models.CASCADE)
    ingredients = models.TextField(default="")
    preparation = models.TextField(default="")
    cooking_method = models.TextField(default="")

    def __str__(self):
        return self.title.title # The first title is a reference to the SignatureRecipe Object, so need the second title to reference the actual CharField

    def recipe_converter(self, subsection):
        """
        A Method that converts each recipe's subsection (Ingredients, Preparation, Cooking Method) input to
        a readable output that the user can see in the view, and returns a dictionary that contains a subheader (if
        it exists) for each subsection as the key, with the list of details as the value of each key

        Parameters:
        -----------
        subsection: str
            Values can only be from {'Ingredients', 'Preparation', 'Cooking Method'}
        """
        # Code block to split the content of each subsection into a list containing each sentence as the elements
        if subsection.lower() == 'ingredients':
            subsection_sentence_list = self.ingredients.split('\r\n')
        elif subsection.lower() == 'preparation':
            subsection_sentence_list = self.preparation.split('\r\n')
        else:
            subsection_sentence_list = self.cooking_method.split('\r\n')

        subsection_subheaders = []
        subsection_details = []

        # Code block to separate out the subheaders (if it exists) from the details of each subsection
        for sentence in subsection_sentence_list:
            try:
                if sentence[-1] == ":":
                    subsection_subheaders.append(sentence)
                else:
                    subsection_details.append(sentence)
            except:
                    subsection_details.append(sentence)

        # Code block specifically for the Preparation or Cooking Method subsection, to remove the number
        # from the sentence
        if subsection.lower() != 'ingredients':
            for i in range(len(subsection_details)):
                try:
                    if int(subsection_details[i][0]): # To capture and remove the number and the ')' from steps 1 to 9
                        subsection_details[i] = subsection_details[i][2:]
                        if subsection_details[i][0] == ')': # To capture the details exceeding 9), from steps 10 to 99
                            subsection_details[i] = subsection_details[i][1:]
                except:
                    pass

        # Code block to append specific details of a subheader to its own list, and grouping all that lists
        # into 1 list
        subsection_subdetails = []
        if subsection.lower() == 'ingredients':
            temp_list = []
            for detail in subsection_details: # Creating a list of lists; the interior list contains the individual bullet point details
                temp_list.append(detail)
                if detail != subsection_details[-1]:
                    if detail == '':
                        subsection_subdetails.append(temp_list)
                        temp_list = []
                    else:
                        pass
                else:
                    subsection_subdetails.append(temp_list)
        else:
            temp_list = []
            sub_bullet_list = []
            for step in subsection_details:
                if 'o\t' in step:
                    sub_bullet_list.append(step[2:])
                    if step != subsection_details[-1]:
                        continue
                    else:
                        temp_list.append(sub_bullet_list)
                        subsection_subdetails.append(temp_list)
                        break
                if len(sub_bullet_list) != 0:
                    temp_list.append(sub_bullet_list)
                    sub_bullet_list = []

                temp_list.append(step)
                if step != subsection_details[-1]:
                    if step == '':
                        subsection_subdetails.append(temp_list)
                        temp_list = []
                    else:
                        pass
                else:
                    subsection_subdetails.append(temp_list)

        # Code block to create a dictionary with the keys as the names of the subheaders and the values will be
        # the corresponding list containing each bullet point / detail for that specific subheader
        subsection_dict = {}
        if len(subsection_subheaders) != 0:
            for i in range(len(subsection_subheaders)):
                subsection_dict[subsection_subheaders[i]] = subsection_subdetails[i]
        else:
            subsection_dict[''] = subsection_subdetails[0]

        return subsection_dict

class PhotoCategory(models.Model):
    class Meta:
        verbose_name_plural = "Photo Categories"

    title = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to="images/Photography/Categories/")

    def __str__(self):
        return self.title

    def hyperlink(self):
        """
        Converts the title to an acceptable hyperlink format and returns that format
        """
        return self.title.replace(' ', '_')

class Photo(models.Model):
    picture = models.ImageField(upload_to="images/Photography/All Photos/") # Pictures added have to be in the landscape / horizontally oriented format for the view to be visually appealing
                                                                            # So no portrait / vertically oriented pictures
    photo_category = models.ForeignKey(PhotoCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class BookGenre(models.Model):
    class Meta:
        verbose_name_plural = "Book Genres"

    title = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to="images/Library/Genres/")

    def __str__(self):
        return self.title

    def hyperlink(self):
        """
        Converts the title to an acceptable hyperlink format and returns that format
        """
        return self.title.replace(' ', '_')

class Book(models.Model):
    book_genre = models.ForeignKey(BookGenre, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="images/Library/All Books/")
    book_review = models.TextField(default="")

    def __str__(self):
        return self.title

class Experience(models.Model):
    experience_type = [
        ("Work Experience", "Work Experience"),
        ("Volunteer Experience", "Volunteer Experience")
    ]

    organization_name = models.CharField(max_length=200)
    organization_logo = models.ImageField(upload_to="images/Experience/")
    background = models.TextField(default="")
    type = models.CharField(max_length=200, choices=experience_type)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    tasks = models.TextField(default="", verbose_name="Tasks (Format: 1), 2)):")
    results = models.TextField(default="", verbose_name="Results (Format: 1), 2)):")

    def __str__(self):
        return self.organization_name

    def date_parser(self):
        """
            A Method that returns a dictionary containing the start and end 'month'
            and 'year' of that experience
        """
        start_month = self.start_date.strftime("%b")
        start_year = self.start_date.year
        end_month = self.end_date.strftime("%b")
        end_year = self.end_date.year

        dict_ = {
            'start_month': start_month,
            'start_year': start_year,
            'end_month': end_month,
            'end_year': end_year,
        }

        return dict_
