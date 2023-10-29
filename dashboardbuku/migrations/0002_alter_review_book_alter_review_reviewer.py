# Generated by Django 4.2.6 on 2023-10-27 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_load_fixtures'),
        ('authentication', '0003_member_match_received_member_match_sent'),
        ('dashboardbuku', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='books.book'),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='authentication.member'),
        ),
    ]