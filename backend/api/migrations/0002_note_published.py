# Generated by Django 4.0.5 on 2022-06-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]