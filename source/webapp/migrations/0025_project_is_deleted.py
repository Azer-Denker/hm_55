# Generated by Django 2.2 on 2021-04-01 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0024_auto_20210327_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
