# Generated by Django 5.1.3 on 2024-11-30 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('Amount', models.IntegerField(default=0)),
                ('Requirements', models.TextField()),
            ],
        ),
    ]
