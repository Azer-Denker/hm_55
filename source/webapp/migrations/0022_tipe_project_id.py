# Generated by Django 2.2 on 2021-03-27 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_remove_tipe_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipe',
            name='project_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='webapp.Project', verbose_name='Проект1'),
            preserve_default=False,
        ),
    ]
