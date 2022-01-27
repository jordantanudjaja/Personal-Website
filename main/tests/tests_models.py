from django.test import TestCase
from ..models import *
import tempfile
import datetime

# This test file tests whether the models in models.py are working as intended by testing
# each method in each model

class TestModels(TestCase):
    def setUp(self):
        # Creating a mock SkillType object
        SkillType.objects.create(
            type = "Web development"
        )

        # Creating a mock Tool object
        Tool.objects.create(
            name = "Django",
            skill_type = SkillType.objects.get(type = "Web development"),
            logo = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

        # Creating a mock ProjectSummary object (1)
        ProjectSummary.objects.create(
            title = "Yugioh Toolbox",
            project_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            summary = "A toolbox for Yugioh",
            github_link = "github.com",
            additional_links = "Yugioh Card Database: www.google.com",
        )

        # Creating a mock ProjectSummary object (2)
        ProjectSummary.objects.create(
            title = "Mycroft",
            project_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            summary = "Sherlock Holmes brother",
            github_link = "github.com",
            additional_links = ""
        )

        # Creating a mock ProjectDetail object
        ProjectDetail.objects.create(
            title = ProjectSummary.objects.get(title = "Yugioh Toolbox"),
            top_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            description = "description",
            tools_used = "tools used",
            middle_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            context = "context",
            goals = "1) Innovation\r\n2) Zone", # To get these \r\n notation, must print raw string in views.py, example: (print(repr(project.goals))). The raw string will show up in the terminal and I can match the format with the test.
            potential_improvements = "1) Hello\r\n2) Bye\r\n51) Bankai",
            bottom_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

        # Creating a mock SignatureRecipe object (1)
        SignatureRecipe.objects.create(
            title = "Freshly Baked Onions with Tempura",
            profile_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

        # Creating a mock SignatureRecipe object (2)
        SignatureRecipe.objects.create(
            title = "IDK just another recipe lol",
            profile_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

        # Creating a mock SignatureRecipe object (3)
        SignatureRecipe.objects.create(
            title = "Another recipe 3",
            profile_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

        # Creating a mock RecipeDetail object (1)
        RecipeDetail.objects.create(
            title = SignatureRecipe.objects.get(title = "Freshly Baked Onions with Tempura"),
            ingredients = "1 pound of ground beef\r\n1 onion\r\n10 cloves of garlic\r\n4 tbsp soy sauce",
            preparation = "1)\tPlace the ground beef in a mixing bowl and flatten and mix it using a spatula\r\n2)\tFinely dice the onion and garlic and mix them thoroughly with the ground beef\r\n3)\tAdd the soy sauce and mirin into the mixing bowl, and season with a pinch of salt and 2 – 3 tbsp of pepper\r\no\tDo not add too much salt because there is already 4 tbsp of soy sauce\r\n4)\tMix the mixture thoroughly\r\no\tOptional Step: Add more pepper after mixing to make the seasoning more uniform\r\n5)\tDice the scallion and set it aside on a separate bowl",
            cooking_method = "Ground Beef Bulgogi:\r\n1)\tHeat up a pan on medium-high heat\r\n2)\tAdd olive oil into the pan\r\n3)\tOnce the oil starts smoking, add in the ground beef mixture\r\n4)\tMix thoroughly using a spatula for 7–8 minutes\r\n5)\tAfter all the beef has turned brown, turn the heat down to medium-low\r\n6)\tAdd the diced scallions into the pan and stir thoroughly for 1 minute\r\n7)\tCarefully strain most of the water and oil mixture from the pan\r\no\tIt is important to do this because the onions will release a lot of water during the heating process\r\n8)\tAdd the sesame seeds and sesame oil to the pan and stir thoroughly for another 2–3 minutes\r\n9)\tTurn off the heat and set the pan aside"
        )

        # Creating a mock RecipeDetail object (2)
        RecipeDetail.objects.create(
            title = SignatureRecipe.objects.get(title = "IDK just another recipe lol"),
            ingredients = "Mushroom buttered rice filling:\r\n1 bowl of white rice\r\n3 cloves of garlic\r\n10–12 slices of mushrooms\r\n-\tSubstitutes: Shitake mushrooms\r\n2 tbsp butter\r\n2 tbsp furikake\r\n2 tsp chives",
            preparation = "1)\tCook a bowl of white rice in a rice cooker\r\n22)\tDebone chicken wings\r\no\tOptional Step: Cut out the drum from the wing and just debone the wing if that makes it easier, but it will result in a smaller pocket for stuffing\r\no\tKeep the bones for making chicken stock\r\n3)\tFinely chop mushrooms and set them aside on a bowl\r\n4)\tChop and dice garlic and set aside on a separate bowl",
            cooking_method = "Marinated chicken wings:\r\n1)\tSeason the chicken wings with smoked paprika\r\n2)\tAdd the dark soy sauce, sugar, and oyster sauce to the chicken wings and knead thoroughly on a bowl\r\n3)\tLeave the chicken wings to marinate for at least 30 minutes\r\n\r\nMushroom buttered rice filling:\r\n1)\tHeat up a pan on high heat\r\no\tDon’t add any oil to it\r\n2)\tAdd the chopped mushrooms and let them sit for 5 minutes \r\no\tPurpose is to boil the water out to concentrate the taste\r\n3)\tOptional Step: Drain excess water from the pan\r\n48)\tAdd in the butter to the pan and stir until it is fully melted\r\n5)\tAdd in the garlic and continue stirring for another 5 minutes\r\n6)\tSeason the pan with salt and pepper\r\n7)\tTurn off the heat and transfer the contents of the pan to a bowl of white rice\r\n8)\tAdd chives, furikake, salt, and pepper into the bowl and mix thoroughly \r\no\tThere should be enough butter so that the mixture is not dry"
        )

        # Creating a mock RecipeDetail object (3)
        RecipeDetail.objects.create(
            title = SignatureRecipe.objects.get(title = "Another recipe 3"),
            ingredients = "3 Servings of Cheese Soufflé:\r\n3 eggs\r\n3 tbsp butter\r\n1 cup of whole milk\r\n1/3 cup of flour\r\n½ cup of grated cheddar cheese\r\n½ cup of grated swiss cheese\r\n¼ cup of grated parmesan cheese\r\n1 tsp cumin\r\n1 tsp paprika\r\n1 tsp nutmeg\r\n3 tbsp breadcrumbs",
            preparation = "Soft-boiled eggs:\r\n1)\tPour cold water on a pot, cover with a lid, and let it come to a rolling boil\r\n2)\tPrepare an ice bath in a large mixing bowl\r\no\tIce-bath will be used to stop the cooking of the eggs immediately after they have finished boiling\r\n3)\tCarefully place the 4 eggs into the pot, cover with a lid and let it boil for exactly 4½ minutes\r\no\tIt is very important to be strict with this timing for a perfect soft-boiled egg\r\n4)\tTake the eggs out and immediately put them in the ice bath to stop the cooking\r\n5)\tLet the eggs cool down for 10–15 minutes\r\n\r\nSausage layer:\r\n1)\tRemove the casing of the sausages and place the sausage meat in a separate mixing bowl, and discard the casing\r\no\tUse a sharp knife to gently cut open the casing, and then peel the rest with your fingers\r\no\tDo not mix in the casing with the sausage meat because they are very chewy and not very pleasant to eat once the scotch egg is cooked\r\n2)\tUse your hands to knead the sausage meat together until they are all fully incorporated into 1 big lump\r\no\tAlternate Step: If using ground pork, knead it until it becomes a giant lump\r\n3)\tAdd in the seasonings and spices to the ground sausage meat / ground pork and use your hands to knead again until the mixture is fully incorporated\r\n4)\tSet aside and let it rest\r\n\r\nBreading Assembly Line:\r\n1)\tCrack open 1 egg into a bowl and whisk thoroughly to make an egg wash \r\n2)\tPour flour and the breadcrumbs into separate bowls\r\n3)\tArrange the bowls in the order of flour, beaten egg mixture, and breadcrumbs as the assembly line",
            cooking_method = "1)\tSeparate 3 egg whites and egg yolks into separate bowls\r\no\tMake sure that no egg yolks are in the egg whites because it will prevent the egg whites from forming stiff peaks when we beat them later\r\n2)\tHeat a pot on medium heat\r\no\tHigh heat can cause the butter to burn\r\n3)\tAdd butter to it and stir until it is fully melted\r\n4)\tAdd flour and stir thoroughly to make a roux\r\n5)\tTurn off the heat and add a bit of milk\r\n6)\tStir with a whisk until solid clumps form \r\n7)\tAdd the remaining milk and whisk until all the solid clumps dissolve\r\n8)\tPut the pot back on medium heat and stir until the mixture thickens\r\n9)\tRemove the pot from the heat\r\n10)\tAdd all the cheese into the pot and stir until all the cheese is melted and it forms a thick mixture\r\n11)\tAdd the spices, and salt into the pot and stir thoroughly\r\n12)\tAdd the egg yolks one by one and stir thoroughly \r\n13)\tPlace the cheese mixture into a large bowl to cool slightly and add pepper to it and mix thoroughly\r\n14)\tPre-heat the oven to 375˚F\r\n15)\tAdd a pinch of salt to the egg whites and whisk thoroughly until stiff peaks form\r\n16)\tPlace some of the egg whites into the cheese mixture and fold gradually\r\no\tIt is important to fold and not mix so that you minimize the disturbance to the whipped egg whites to retain the whipped in air and the volume of the mixture\r\no\tEven when folding, some volume will be lost, but the goal is to minimize this so that the soufflé does not deflate easily after taking it out of the oven\r\n17)\tContinue adding egg whites into the cheese mixture and fold periodically\r\n18)\tTake out the ramekins and divide the cheese mixture evenly among all the ramekins\r\n19)\tSprinkle grated parmesan or cheddar cheese on top\r\n20)\t Place the ramekins on top of a baking tray and place them in the oven to bake for 25–30 minutes\r\n21)\tTake out the oven and serve while hot\r\no\tIt will deflate if left at room temperature for too long"
        )

        # Creating a mock PhotoCategory object
        PhotoCategory.objects.create(
            title = "Portrait",
            profile_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

        # Creating a mock Photo object
        Photo.objects.create(
            picture = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_category = PhotoCategory.objects.get(title = "Portrait"),
            title = "My face"
        )

        # Creating a mock BookGenre object
        BookGenre.objects.create(
            title = "American literature",
            profile_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

        # Creating a mock Book object
        Book.objects.create(
            book_genre = BookGenre.objects.get(title = "American literature"),
            title = "Birds and the bees",
            author = "DJ Aron",
            picture = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            book_review = "This is pretty meh"
        )

        # Creating a mock Experience object
        Experience.objects.create(
            organization_name = "My Organization",
            organization_logo = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            background = "My organization is none of your business lol",
            type = "Work Experience",
            role = "CEO",
            start_date = datetime.date(2019, 3, 25),
            end_date = datetime.date(2020, 12, 10),
            tasks = "1)\tAttack and Defend\r\n22)\tDo Nothing",
            results = "14)\tPlay Chess Mister Bankai\r\n8)\tThen smoke some weed"
        )

        # Getting the objects in each mocked model and storing it in a variable in this TestModels Class so that it can be called on different tests as appropriate
        self.skill_type_1 = SkillType.objects.get(pk=1)
        self.tool_1 = Tool.objects.get(pk=1)

        self.project_summary_1 = ProjectSummary.objects.get(pk=1)
        self.project_summary_2 = ProjectSummary.objects.get(pk=2)

        self.project_detail_1 = ProjectDetail.objects.get(title = self.project_summary_1)

        self.signature_recipe_1 = SignatureRecipe.objects.get(pk=1)
        self.signature_recipe_2 = SignatureRecipe.objects.get(pk=2)
        self.signature_recipe_3 = SignatureRecipe.objects.get(pk=3)

        self.recipe_detail_1 = RecipeDetail.objects.get(title=self.signature_recipe_1)
        self.recipe_detail_2 = RecipeDetail.objects.get(title=self.signature_recipe_2)
        self.recipe_detail_3 = RecipeDetail.objects.get(title=self.signature_recipe_3)

        self.photo_category_1 = PhotoCategory.objects.get(pk=1)
        self.photo_1 = Photo.objects.get(photo_category=self.photo_category_1)

        self.book_genre_1 = BookGenre.objects.get(pk=1)
        self.book_1 = Book.objects.get(book_genre=self.book_genre_1)

        self.experience_1 = Experience.objects.get(pk=1)

    def test_SkillType___str___method(self):
        self.assertEqual(str(self.skill_type_1), self.skill_type_1.type)

    def test_Tool___str___method(self):
        self.assertEqual(str(self.tool_1), self.tool_1.name)

    def test_ProjectSummary___str___method(self):
        self.assertEqual(str(self.project_summary_1), self.project_summary_1.title)
        self.assertEqual(str(self.project_summary_2), self.project_summary_2.title)

    def test_ProjectSummary_hyperlink_method(self):
        self.assertEqual(self.project_summary_1.hyperlink(), "Yugioh_Toolbox")
        self.assertEqual(self.project_summary_2.hyperlink(), "Mycroft")

    def test_ProjectSummary_link_converter_method(self):
        self.assertEqual(self.project_summary_1.link_converter(), {"Yugioh Card Database": "www.google.com"})
        self.assertEqual(self.project_summary_2.link_converter(), "")

    def test_ProjectDetail___str___method(self):
        self.assertEqual(str(self.project_detail_1), self.project_detail_1.title.title)

    def test_ProjectDetail_list_preprocessor_method(self):
        self.assertEqual(self.project_detail_1.list_preprocessor('Goals'), ["Innovation", "Zone"])
        self.assertEqual(self.project_detail_1.list_preprocessor('Potential Improvements'), ["Hello", "Bye", "Bankai"])

    def test_SignatureRecipe___str___method(self):
        self.assertEqual(str(self.signature_recipe_1), self.signature_recipe_1.title)
        self.assertEqual(str(self.signature_recipe_2), self.signature_recipe_2.title)
        self.assertEqual(str(self.signature_recipe_3), self.signature_recipe_3.title)

    def test_SignatureRecipe_hyperlink_method(self):
        self.assertEqual(self.signature_recipe_1.hyperlink(), "Freshly_Baked_Onions_with_Tempura")
        self.assertEqual(self.signature_recipe_2.hyperlink(), "IDK_just_another_recipe_lol")
        self.assertEqual(self.signature_recipe_3.hyperlink(), "Another_recipe_3")

    def test_RecipeDetail___str___method(self):
        self.assertEqual(str(self.recipe_detail_1), self.recipe_detail_1.title.title)
        self.assertEqual(str(self.recipe_detail_2), self.recipe_detail_2.title.title)
        self.assertEqual(str(self.recipe_detail_3), self.recipe_detail_3.title.title)

    def test_RecipeDetail_recipe_converter_method(self):
        # Testing recipe_detail_1
        self.assertEqual(self.recipe_detail_1.recipe_converter('Ingredients'), {'': ['1 pound of ground beef',
                                                                                     '1 onion',
                                                                                     '10 cloves of garlic',
                                                                                     '4 tbsp soy sauce']})

        self.assertEqual(self.recipe_detail_1.recipe_converter('Preparation'), {'': ['\tPlace the ground beef in a mixing bowl and flatten and mix it using a spatula',
                                                                                     '\tFinely dice the onion and garlic and mix them thoroughly with the ground beef',
                                                                                     '\tAdd the soy sauce and mirin into the mixing bowl, and season with a pinch of salt and 2 – 3 tbsp of pepper',
                                                                                     ['Do not add too much salt because there is already 4 tbsp of soy sauce'],
                                                                                     '\tMix the mixture thoroughly',
                                                                                     ['Optional Step: Add more pepper after mixing to make the seasoning more uniform'],
                                                                                     '\tDice the scallion and set it aside on a separate bowl']})

        self.assertEqual(self.recipe_detail_1.recipe_converter('Cooking Method'), {'Ground Beef Bulgogi:': ['\tHeat up a pan on medium-high heat',
                                                                                                            '\tAdd olive oil into the pan',
                                                                                                            '\tOnce the oil starts smoking, add in the ground beef mixture',
                                                                                                            '\tMix thoroughly using a spatula for 7–8 minutes',
                                                                                                            '\tAfter all the beef has turned brown, turn the heat down to medium-low',
                                                                                                            '\tAdd the diced scallions into the pan and stir thoroughly for 1 minute',
                                                                                                            '\tCarefully strain most of the water and oil mixture from the pan',
                                                                                                            ['It is important to do this because the onions will release a lot of water during the heating process'],
                                                                                                            '\tAdd the sesame seeds and sesame oil to the pan and stir thoroughly for another 2–3 minutes',
                                                                                                            '\tTurn off the heat and set the pan aside']})

        # Testing recipe_detail_2
        self.assertEqual(self.recipe_detail_2.recipe_converter('Ingredients'), {'Mushroom buttered rice filling:': ['1 bowl of white rice',
                                                                                                                    '3 cloves of garlic',
                                                                                                                    '10–12 slices of mushrooms',
                                                                                                                    '-\tSubstitutes: Shitake mushrooms',
                                                                                                                    '2 tbsp butter',
                                                                                                                    '2 tbsp furikake',
                                                                                                                    '2 tsp chives']})

        self.assertEqual(self.recipe_detail_2.recipe_converter('Preparation'), {'': ['\tCook a bowl of white rice in a rice cooker',
                                                                                     '\tDebone chicken wings',
                                                                                     ['Optional Step: Cut out the drum from the wing and just debone the wing if that makes it easier, but it will result in a smaller pocket for stuffing',
                                                                                      'Keep the bones for making chicken stock'],
                                                                                     '\tFinely chop mushrooms and set them aside on a bowl',
                                                                                     '\tChop and dice garlic and set aside on a separate bowl']})

        self.assertEqual(self.recipe_detail_2.recipe_converter('Cooking Method'), {'Marinated chicken wings:': ['\tSeason the chicken wings with smoked paprika',
                                                                                                               '\tAdd the dark soy sauce, sugar, and oyster sauce to the chicken wings and knead thoroughly on a bowl',
                                                                                                               '\tLeave the chicken wings to marinate for at least 30 minutes',
                                                                                                               ''],
                                                                                  'Mushroom buttered rice filling:': ['\tHeat up a pan on high heat',
                                                                                                                      ['Don’t add any oil to it'],
                                                                                                                      '\tAdd the chopped mushrooms and let them sit for 5 minutes ',
                                                                                                                      ['Purpose is to boil the water out to concentrate the taste'],
                                                                                                                      '\tOptional Step: Drain excess water from the pan',
                                                                                                                      '\tAdd in the butter to the pan and stir until it is fully melted',
                                                                                                                      '\tAdd in the garlic and continue stirring for another 5 minutes',
                                                                                                                      '\tSeason the pan with salt and pepper',
                                                                                                                      '\tTurn off the heat and transfer the contents of the pan to a bowl of white rice',
                                                                                                                      '\tAdd chives, furikake, salt, and pepper into the bowl and mix thoroughly ',
                                                                                                                      ['There should be enough butter so that the mixture is not dry']]})

        # Testing recipe_detail_3
        self.assertEqual(self.recipe_detail_3.recipe_converter('Ingredients'), {'3 Servings of Cheese Soufflé:': ['3 eggs',
                                                                                                                  '3 tbsp butter',
                                                                                                                  '1 cup of whole milk',
                                                                                                                  '1/3 cup of flour',
                                                                                                                  '½ cup of grated cheddar cheese',
                                                                                                                  '½ cup of grated swiss cheese',
                                                                                                                  '¼ cup of grated parmesan cheese',
                                                                                                                  '1 tsp cumin',
                                                                                                                  '1 tsp paprika',
                                                                                                                  '1 tsp nutmeg',
                                                                                                                  '3 tbsp breadcrumbs']})

        self.assertEqual(self.recipe_detail_3.recipe_converter('Preparation'), {'Soft-boiled eggs:': ['\tPour cold water on a pot, cover with a lid, and let it come to a rolling boil',
                                                                                                      '\tPrepare an ice bath in a large mixing bowl',
                                                                                                      ['Ice-bath will be used to stop the cooking of the eggs immediately after they have finished boiling'],
                                                                                                      '\tCarefully place the 4 eggs into the pot, cover with a lid and let it boil for exactly 4½ minutes',
                                                                                                      ['It is very important to be strict with this timing for a perfect soft-boiled egg'],
                                                                                                      '\tTake the eggs out and immediately put them in the ice bath to stop the cooking',
                                                                                                      '\tLet the eggs cool down for 10–15 minutes', ''],
                                                                                'Sausage layer:': ['\tRemove the casing of the sausages and place the sausage meat in a separate mixing bowl, and discard the casing',
                                                                                                   ['Use a sharp knife to gently cut open the casing, and then peel the rest with your fingers',
                                                                                                    'Do not mix in the casing with the sausage meat because they are very chewy and not very pleasant to eat once the scotch egg is cooked'],
                                                                                                   '\tUse your hands to knead the sausage meat together until they are all fully incorporated into 1 big lump',
                                                                                                   ['Alternate Step: If using ground pork, knead it until it becomes a giant lump'],
                                                                                                   '\tAdd in the seasonings and spices to the ground sausage meat / ground pork and use your hands to knead again until the mixture is fully incorporated',
                                                                                                   '\tSet aside and let it rest', ''],
                                                                                'Breading Assembly Line:': ['\tCrack open 1 egg into a bowl and whisk thoroughly to make an egg wash ',
                                                                                                            '\tPour flour and the breadcrumbs into separate bowls',
                                                                                                            '\tArrange the bowls in the order of flour, beaten egg mixture, and breadcrumbs as the assembly line']})

        self.assertEqual(self.recipe_detail_3.recipe_converter('Cooking Method'), {'': ['\tSeparate 3 egg whites and egg yolks into separate bowls',
                                                                                        ['Make sure that no egg yolks are in the egg whites because it will prevent the egg whites from forming stiff peaks when we beat them later'],
                                                                                        '\tHeat a pot on medium heat', ['High heat can cause the butter to burn'],
                                                                                        '\tAdd butter to it and stir until it is fully melted',
                                                                                        '\tAdd flour and stir thoroughly to make a roux',
                                                                                        '\tTurn off the heat and add a bit of milk',
                                                                                        '\tStir with a whisk until solid clumps form ',
                                                                                        '\tAdd the remaining milk and whisk until all the solid clumps dissolve',
                                                                                        '\tPut the pot back on medium heat and stir until the mixture thickens',
                                                                                        '\tRemove the pot from the heat',
                                                                                        '\tAdd all the cheese into the pot and stir until all the cheese is melted and it forms a thick mixture',
                                                                                        '\tAdd the spices, and salt into the pot and stir thoroughly',
                                                                                        '\tAdd the egg yolks one by one and stir thoroughly ',
                                                                                        '\tPlace the cheese mixture into a large bowl to cool slightly and add pepper to it and mix thoroughly',
                                                                                        '\tPre-heat the oven to 375˚F',
                                                                                        '\tAdd a pinch of salt to the egg whites and whisk thoroughly until stiff peaks form',
                                                                                        '\tPlace some of the egg whites into the cheese mixture and fold gradually',
                                                                                        ['It is important to fold and not mix so that you minimize the disturbance to the whipped egg whites to retain the whipped in air and the volume of the mixture',
                                                                                         'Even when folding, some volume will be lost, but the goal is to minimize this so that the soufflé does not deflate easily after taking it out of the oven'],
                                                                                        '\tContinue adding egg whites into the cheese mixture and fold periodically',
                                                                                        '\tTake out the ramekins and divide the cheese mixture evenly among all the ramekins',
                                                                                        '\tSprinkle grated parmesan or cheddar cheese on top',
                                                                                        '\t Place the ramekins on top of a baking tray and place them in the oven to bake for 25–30 minutes',
                                                                                        '\tTake out the oven and serve while hot',
                                                                                        ['It will deflate if left at room temperature for too long']]})

    def test_PhotoCategory___str___method(self):
        self.assertEqual(str(self.photo_category_1), self.photo_category_1.title)

    def test_PhotoCategory_hyperlink_method(self):
        self.assertEqual(self.photo_category_1.hyperlink(), "Portrait")

    def test_Photo___str___method(self):
        self.assertEqual(str(self.photo_1), self.photo_1.title)

    def test_BookGenre___str___method(self):
        self.assertEqual(str(self.book_genre_1), self.book_genre_1.title)

    def test_BookGenre_hyperlink_method(self):
        self.assertEqual(self.book_genre_1.hyperlink(), "American_literature")

    def test_Book___str___method(self):
        self.assertEqual(str(self.book_1), self.book_1.title)

    def test_Experience___str___method(self):
        self.assertEqual(str(self.experience_1), self.experience_1.organization_name)

    def test_Experience_date_parser_method(self):
        self.assertEqual(self.experience_1.date_parser(), {'start_month': 'Mar',
                                                           'start_year': 2019,
                                                           'end_month': 'Dec',
                                                           'end_year': 2020,})
