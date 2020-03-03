# Generated by Django 3.0.3 on 2020-03-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=150)),
                ('image', models.URLField()),
                ('released', models.IntegerField(max_length=4)),
                ('runtime', models.CharField(max_length=8)),
                ('imdb_id', models.CharField(max_length=150)),
            ],
        ),
    ]
