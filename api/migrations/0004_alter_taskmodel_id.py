# Generated by Django 3.2.9 on 2021-11-11 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_taskmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
