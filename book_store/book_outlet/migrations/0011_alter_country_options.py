# Generated by Django 3.2.5 on 2022-07-11 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0010_alter_country_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
    ]
