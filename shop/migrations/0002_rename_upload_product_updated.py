# Generated by Django 4.0.4 on 2022-05-09 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='upload',
            new_name='updated',
        ),
    ]