# Generated by Django 4.2 on 2023-04-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]