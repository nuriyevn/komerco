# Generated by Django 2.1.3 on 2018-12-12 09:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_logo',
            field=models.CharField(default=django.utils.timezone.now, max_length=600),
            preserve_default=False,
        ),
    ]
