# Generated by Django 3.1 on 2020-09-01 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MustufaJan', '0012_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500)),
                ('level', models.PositiveIntegerField(default=10)),
                ('years', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
