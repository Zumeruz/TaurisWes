# Generated by Django 5.1.4 on 2025-03-03 10:53

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_book'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.about')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Forma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('destination', models.CharField(choices=[('usa', 'USA'), ('italy', 'Italiy'), ('china', 'China'), ('japan', 'Japan'), ('mexicO', 'Mexico')], default='usa', max_length=500)),
                ('request', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
