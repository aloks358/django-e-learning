# Generated by Django 2.0.5 on 2019-06-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
