# Generated by Django 4.0.6 on 2022-08-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs', '0006_alter_card_battle_cry_alter_card_card_about_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archetype',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
