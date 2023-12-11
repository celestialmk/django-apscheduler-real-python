# Generated by Django 3.2.6 on 2023-12-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('link', models.URLField()),
                ('image', models.URLField()),
                ('podcast_name', models.CharField(max_length=100)),
                ('guid', models.CharField(max_length=50)),
            ],
        ),
    ]
