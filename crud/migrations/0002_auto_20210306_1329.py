# Generated by Django 3.1.7 on 2021-03-06 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subcategory',
            new_name='CategorySub',
        ),
    ]