# Generated by Django 2.2.4 on 2024-07-13 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_authorandBooks', '0002_auto_20240713_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='app_authorandBooks.Book'),
        ),
    ]
