# Generated by Django 4.2.6 on 2023-11-06 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_user_logins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='logins',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
