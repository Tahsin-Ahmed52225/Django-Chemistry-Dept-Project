# Generated by Django 4.0.4 on 2022-07-15 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0006_alter_research_publication_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='publication_video',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='research',
            name='research_title',
            field=models.CharField(max_length=250),
        ),
    ]