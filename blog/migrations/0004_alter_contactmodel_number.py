# Generated by Django 5.0.2 on 2024-02-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_contactmodel_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='number',
            field=models.CharField(max_length=10),
        ),
    ]
