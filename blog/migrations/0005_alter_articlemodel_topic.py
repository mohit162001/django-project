# Generated by Django 5.0.2 on 2024-02-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_contactmodel_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='topic',
            field=models.CharField(max_length=20),
        ),
    ]