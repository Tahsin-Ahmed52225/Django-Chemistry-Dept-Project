# Generated by Django 4.0.4 on 2022-09-10 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0014_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_title', models.TextField(max_length=100)),
                ('award_discription', models.TextField(max_length=100)),
                ('award_url', models.TextField(max_length=100)),
                ('award_cover', models.ImageField(blank=True, null=True, upload_to='Images/')),
            ],
        ),
    ]