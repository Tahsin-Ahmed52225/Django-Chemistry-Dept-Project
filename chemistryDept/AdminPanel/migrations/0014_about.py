# Generated by Django 4.0.4 on 2022-09-10 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0013_banner_banner_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_description', models.TextField(max_length=100)),
                ('about_url', models.TextField(max_length=100)),
            ],
        ),
    ]
