# Generated by Django 3.2.3 on 2021-10-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210824_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='filter',
            field=models.CharField(choices=[('DRINKS', 'DRINKS'), ('LUNCH', 'LUNCH'), ('DINNER', 'DINNER')], max_length=200, null=True),
        ),
    ]
