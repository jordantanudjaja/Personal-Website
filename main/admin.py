from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(SkillType)
admin.site.register(Tool)
admin.site.register(ProjectSummary)
admin.site.register(ProjectDetail)
admin.site.register(SignatureRecipe)
admin.site.register(RecipeDetail)
admin.site.register(PhotoCategory)
admin.site.register(Photo)
admin.site.register(BookGenre)
admin.site.register(Book)
admin.site.register(Experience)
