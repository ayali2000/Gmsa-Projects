# Generated by Django 4.1.3 on 2022-12-17 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hadith',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
