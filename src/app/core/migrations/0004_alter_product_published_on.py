# Generated by Django 5.0.7 on 2024-07-26 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_product_published_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
