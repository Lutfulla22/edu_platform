# Generated by Django 4.1.5 on 2023-01-09 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_alter_course_course_photo_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]