# Generated by Django 5.1.4 on 2025-02-21 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=2000)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('offer', models.CharField(max_length=50)),
                ('offer2', models.CharField(max_length=50)),
                ('offfer3', models.CharField(max_length=50)),
            ],
        ),
    ]
