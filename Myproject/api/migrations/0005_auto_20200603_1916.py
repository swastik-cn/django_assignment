# Generated by Django 3.0.6 on 2020-06-03 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200603_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.Mentor'),
        ),
    ]