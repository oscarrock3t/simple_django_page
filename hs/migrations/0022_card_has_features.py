# Generated by Django 4.0.6 on 2022-08-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs', '0021_cardfeature_card_cardfeature_feature_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='has_features',
            field=models.BooleanField(default=False, verbose_name='Способности'),
        ),
    ]
