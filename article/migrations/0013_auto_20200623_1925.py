# Generated by Django 3.0.6 on 2020-06-23 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20200623_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tags',
            new_name='tag',
        ),
    ]