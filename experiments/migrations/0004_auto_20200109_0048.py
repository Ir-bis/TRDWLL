# Generated by Django 3.0.2 on 2020-01-09 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0003_auto_20190605_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='image',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='is_featured',
        ),
        migrations.AlterField(
            model_name='experiment',
            name='published_date',
            field=models.DateTimeField(help_text='When was this project created?'),
        ),
    ]
