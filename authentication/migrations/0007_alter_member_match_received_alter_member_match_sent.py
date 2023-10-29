# Generated by Django 4.2.6 on 2023-10-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_member_match_received_alter_member_match_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='match_received',
            field=models.ManyToManyField(blank=True, default=None, to='authentication.member'),
        ),
        migrations.AlterField(
            model_name='member',
            name='match_sent',
            field=models.ManyToManyField(blank=True, default=None, to='authentication.member'),
        ),
    ]