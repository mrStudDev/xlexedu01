# Generated by Django 5.0.4 on 2024-05-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_articles', '0003_articlesmodel_meta_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesmodel',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
