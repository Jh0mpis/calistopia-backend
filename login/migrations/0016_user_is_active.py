# Generated by Django 4.2.5 on 2023-10-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_user_lastloginattemptdate_user_todayloginattempts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
