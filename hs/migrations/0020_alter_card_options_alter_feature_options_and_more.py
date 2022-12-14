# Generated by Django 4.0.6 on 2022-08-01 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hs', '0019_cardfeature_feature_remove_card_battle_cry_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': 'название карты', 'verbose_name_plural': 'Карты'},
        ),
        migrations.AlterModelOptions(
            name='feature',
            options={'verbose_name': 'название свойства', 'verbose_name_plural': 'Свойства'},
        ),
        migrations.AlterField(
            model_name='archetype',
            name='name',
            field=models.CharField(max_length=15, verbose_name='Название архетипа'),
        ),
        migrations.AlterField(
            model_name='card',
            name='archetype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hs.archetype', verbose_name='Архетип'),
        ),
        migrations.AlterField(
            model_name='card',
            name='attack',
            field=models.IntegerField(blank=True, verbose_name='Атака'),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_about',
            field=models.CharField(blank=True, max_length=100, verbose_name='Описание карты'),
        ),
        migrations.AlterField(
            model_name='card',
            name='health',
            field=models.IntegerField(blank=True, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.TextField(blank=True, verbose_name='Ссылка на картинку'),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Название карты'),
        ),
        migrations.AlterField(
            model_name='card',
            name='tavern_level',
            field=models.IntegerField(blank=True, default=1, verbose_name='Уровень таверны'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='feature_disc',
            field=models.CharField(max_length=30, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Свойство'),
        ),
    ]
