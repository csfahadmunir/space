# Generated by Django 3.2.9 on 2021-12-13 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userscore', '0006_remove_user_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
