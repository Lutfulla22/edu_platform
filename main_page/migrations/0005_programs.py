# Generated by Django 4.1.5 on 2023-01-12 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_alter_course_course_photo_delete_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema_uroka', models.CharField(max_length=150)),
                ('opisaniye_temi', models.TextField()),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.course')),
            ],
        ),
    ]