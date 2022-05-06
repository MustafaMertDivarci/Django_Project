# Generated by Django 4.0.4 on 2022-04-29 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kurs adını yazınız', max_length=200, unique=True, verbose_name='Kursun Adı')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='courses/default.gif', upload_to='courses/%Y/%m/%d/')),
                ('date', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
