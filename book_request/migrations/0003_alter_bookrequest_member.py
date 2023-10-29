# Generated by Django 4.2.6 on 2023-10-27 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_member_match_received_member_match_sent'),
        ('book_request', '0002_bookrequest_delete_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrequest',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='authentication.member'),
        ),
    ]