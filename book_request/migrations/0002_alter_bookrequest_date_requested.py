# Generated by Django 4.2.6 on 2023-12-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrequest',
            name='date_requested',
            field=models.DateField(auto_now_add=True),
        ),
    ]
