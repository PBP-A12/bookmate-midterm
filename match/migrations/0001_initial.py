# Generated by Django 4.2.6 on 2023-12-19 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_load_fixtures'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matched_at', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('matched_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matched_member', to='authentication.member')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matching_user', to='authentication.member')),
            ],
        ),
    ]
