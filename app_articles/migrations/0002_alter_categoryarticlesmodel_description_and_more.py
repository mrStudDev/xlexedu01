# Generated by Django 5.0.4 on 2024-04-27 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryarticlesmodel',
            name='description',
            field=models.CharField(max_length=160),
        ),
        migrations.AlterField(
            model_name='categoryarticlesmodel',
            name='name',
            field=models.CharField(max_length=155),
        ),
        migrations.AlterField(
            model_name='tagarticlesmodel',
            name='description',
            field=models.CharField(max_length=160),
        ),
        migrations.AlterField(
            model_name='tagarticlesmodel',
            name='name',
            field=models.CharField(max_length=155),
        ),
    ]
