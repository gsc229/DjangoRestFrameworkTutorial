# Generated by Django 3.0.6 on 2020-05-18 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='lineos',
            new_name='linenos',
        ),
    ]