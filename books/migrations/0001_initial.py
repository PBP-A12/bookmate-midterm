# Generated by Django 4.2.6 on 2023-12-18 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('subjects', models.ManyToManyField(to='authentication.subject')),
            ],
        ),
    ]
