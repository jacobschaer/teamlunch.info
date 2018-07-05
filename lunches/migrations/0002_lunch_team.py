# Generated by Django 2.0.6 on 2018-07-05 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        ('lunches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lunch',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lunches', to='teams.Team'),
        ),
    ]
