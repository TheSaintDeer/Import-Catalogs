# Generated by Django 5.0.7 on 2024-07-26 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_product_published_on'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductAttribute',
            new_name='ProductAttributes',
        ),
    ]
