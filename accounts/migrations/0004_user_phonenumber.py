# Generated by Django 4.0.1 on 2023-03-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='PhoneNumber',
            field=models.CharField(default='hello', error_messages={'required': 'Phone Number must be provided'}, max_length=10),
            preserve_default=False,
        ),
    ]
