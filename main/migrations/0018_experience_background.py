# Generated by Django 3.2.7 on 2021-12-08 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_experience_organization_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='background',
            field=models.TextField(default=''),
        ),
    ]
