# Generated by Django 2.2.7 on 2020-04-14 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200320_0849'),
    ]

    operations = [
        migrations.DeleteModel(
            name='category',
        ),
    ]