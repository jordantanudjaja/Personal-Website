# Generated by Django 3.2.7 on 2022-01-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20220116_0427'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookgenre',
            options={'verbose_name_plural': 'Book Genres'},
        ),
        migrations.AlterField(
            model_name='bookgenre',
            name='profile_picture',
            field=models.ImageField(upload_to='images/Library/Genres/'),
        ),
    ]
