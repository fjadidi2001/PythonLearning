# Generated by Django 4.2 on 2023-04-24 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='offer',
            name='des',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='offer',
            name='dis',
            field=models.FloatField(),
        ),
    ]
