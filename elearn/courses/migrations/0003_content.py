# Generated by Django 2.0.5 on 2019-06-12 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('courses', '0002_auto_20190612_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_type', to='contenttypes.ContentType')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='courses.Module')),
            ],
        ),
    ]