# Generated by Django 4.1.7 on 2023-05-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0004_questionhistory_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionhistory',
            name='answer',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
