# Generated by Django 4.0.6 on 2022-08-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs', '0004_archetype_rename_discription_card_card_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='archetype',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
