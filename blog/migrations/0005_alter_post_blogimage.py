# Generated by Django 4.0 on 2022-02-19 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_blog_image_post_blogimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blogimage',
            field=models.ImageField(blank=True, upload_to='blog_image/'),
        ),
    ]
