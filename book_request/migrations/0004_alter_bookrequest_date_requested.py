# Generated by Django 5.0 on 2023-12-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_request', '0003_bookrequest_subjects_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrequest',
            name='date_requested',
            field=models.DateField(auto_now=True),
        ),
    ]