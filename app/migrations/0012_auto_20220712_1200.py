# Generated by Django 3.1.3 on 2022-07-12 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20220708_1243'),
        ('app', '0011_status_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='last_updated',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.teacher'),
        ),
    ]
