# Generated by Django 4.2.2 on 2023-07-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_conclusion'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='publisher',
            field=models.CharField(default='', max_length=100),
        ),
    ]