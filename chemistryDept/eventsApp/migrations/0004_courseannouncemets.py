# Generated by Django 4.0.4 on 2022-09-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsApp', '0003_seminer_seminer_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseAnnouncemets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.TextField(max_length=200)),
                ('instructor_name', models.TextField(max_length=200)),
                ('course_description', models.TextField()),
                ('number_of_credit', models.IntegerField()),
                ('course_content', models.TextField()),
            ],
        ),
    ]