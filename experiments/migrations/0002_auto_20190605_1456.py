# Generated by Django 2.2.1 on 2019-06-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='tech_used',
            field=models.CharField(default='', help_text='Tech that was used for this experiment.', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experiment',
            name='is_featured',
            field=models.BooleanField(default=False, help_text='Do you want this post to be displayed as a featured experiment on the homepage?'),
        ),
    ]
