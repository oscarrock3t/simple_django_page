# Generated by Django 4.0.6 on 2022-08-01 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs', '0016_alter_card_card_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='battle_cry',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='death_rattle',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='sorcery',
            field=models.BooleanField(default=False),
        ),
    ]
