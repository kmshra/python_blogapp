# Generated by Django 4.0 on 2022-02-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('contact', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('course', models.CharField(max_length=50)),
                ('remarks', models.TextField()),
            ],
        ),
    ]
