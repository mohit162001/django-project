# Generated by Django 5.0.2 on 2024-03-01 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_articlemodel_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='content',
            field=models.CharField(default='This is the content', max_length=300),
        ),
    ]