# Generated by Django 4.1.7 on 2023-04-25 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JLPT', '0002_auto_20230425_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default='', max_length=11),
        ),
    ]