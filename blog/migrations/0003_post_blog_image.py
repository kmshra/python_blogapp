# Generated by Django 4.0 on 2022-02-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_image',
            field=models.ImageField(default=1, upload_to='blog_image'),
            preserve_default=False,
        ),
    ]
