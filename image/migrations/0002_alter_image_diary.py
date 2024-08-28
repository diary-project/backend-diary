# Generated by Django 5.1 on 2024-08-28 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_alter_diary_date'),
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='diary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.diary', unique=True),
        ),
    ]
