# Generated by Django 4.0.6 on 2022-08-01 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hs', '0020_alter_card_options_alter_feature_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardfeature',
            name='card',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hs.card', verbose_name='Карта'),
        ),
        migrations.AddField(
            model_name='cardfeature',
            name='feature',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hs.feature', verbose_name='Свойство'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='feature_disc',
            field=models.CharField(max_length=50, verbose_name='Краткое описание'),
        ),
    ]