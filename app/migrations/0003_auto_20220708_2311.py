# Generated by Django 3.1.3 on 2022-07-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220708_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='status',
            field=models.CharField(choices=[('Submitted', 'Submitted'), ('Checking', 'Checking'), ('Solved', 'Solved'), ('Closed', 'Closed')], default='Submitted', max_length=10),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
