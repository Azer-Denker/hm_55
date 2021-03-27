# Generated by Django 2.2 on 2021-03-27 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipe',
            name='project_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='webapp.Project', verbose_name='Проект'),
            preserve_default=False,
        ),
    ]