# Generated by Django 3.2.7 on 2021-12-07 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_experience_organization_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='organization_logo',
            field=models.ImageField(default='', upload_to='images/Experience/'),
        ),
    ]
