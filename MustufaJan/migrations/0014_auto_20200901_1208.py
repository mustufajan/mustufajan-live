# Generated by Django 3.1 on 2020-09-01 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MustufaJan', '0013_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
