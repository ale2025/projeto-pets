# Generated by Django 3.0.2 on 2020-01-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dono', '0001_initial'),
        ('gatinho', '0004_auto_20200110_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatinho',
            name='dono',
            field=models.ManyToManyField(to='dono.Dono'),
        ),
    ]
