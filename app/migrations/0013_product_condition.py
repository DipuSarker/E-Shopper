# Generated by Django 3.2.7 on 2021-09-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_product_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('New Version', 'New Version'), ('Old Version', 'Old Version'), ('Latest Version', 'Latest Version')], max_length=100, null=True),
        ),
    ]
