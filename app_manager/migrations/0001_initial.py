# Generated by Django 5.0.4 on 2024-04-27 04:26

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=255)),
                ('view_count', models.IntegerField(default=0)),
                ('last_accessed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DailyPageView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('view_count', models.IntegerField(default=1)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_manager.pageview')),
            ],
            options={
                'unique_together': {('page', 'date')},
            },
        ),
    ]
