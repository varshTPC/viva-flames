# Generated by Django 4.0.4 on 2022-04-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viva_app1', '0004_contact_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='flames',
            name='result',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
    ]