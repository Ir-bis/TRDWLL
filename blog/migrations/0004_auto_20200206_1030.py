# Generated by Django 3.0.2 on 2020-02-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, help_text='A short description for the category.', max_length=200, null=True),
        ),
    ]