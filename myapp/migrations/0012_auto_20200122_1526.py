# Generated by Django 2.2.7 on 2020-01-22 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20200122_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='rank',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='url',
            name='ziip',
            field=models.IntegerField(),
        ),
    ]
