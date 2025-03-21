# Generated by Django 5.1.4 on 2025-02-25 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_meet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contry', models.CharField(max_length=50)),
                ('text', models.TextField(blank=True)),
                ('img', models.ImageField(upload_to='index/img')),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='img',
            field=models.ImageField(upload_to='index/img'),
        ),
        migrations.AlterField(
            model_name='about',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='avesome',
            name='data',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='avesome',
            name='img',
            field=models.ImageField(upload_to='index/img'),
        ),
        migrations.AlterField(
            model_name='avesome',
            name='nomber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='avesome',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='easy',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='meet',
            name='img',
            field=models.ImageField(upload_to='index/img'),
        ),
        migrations.AlterField(
            model_name='our',
            name='text',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='popular',
            name='img',
            field=models.ImageField(upload_to='index/img'),
        ),
    ]
