# Generated by Django 5.0.4 on 2024-05-04 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='principiosmodel',
            name='meta_title',
            field=models.CharField(default='Princípios do Direito', max_length=60),
        ),
    ]