# Generated by Django 3.1 on 2020-10-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]