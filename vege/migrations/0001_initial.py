# Generated by Django 5.0.10 on 2025-01-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_discription', models.TextField()),
                ('recipe_img', models.ImageField(upload_to='recipe')),
            ],
        ),
    ]