# Generated by Django 3.0.6 on 2020-06-03 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_mentor_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='mentees',
            field=models.ManyToManyField(blank=True, default=None, to='api.User'),
        ),
        migrations.AlterField(
            model_name='project',
            name='mentor',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='api.Mentor'),
        ),
    ]
