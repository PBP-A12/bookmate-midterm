# Generated by Django 4.2.6 on 2023-10-30 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('bio', models.CharField(max_length=255)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.member')),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-29 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0003_member_match_received_member_match_sent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('bio', models.CharField(max_length=255)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.member')),
            ],
        ),
    ]
