# Generated by Django 4.0.6 on 2022-08-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('image', models.TextField(blank=True)),
                ('discription', models.TextField()),
                ('archetype', models.TextField()),
                ('attack', models.IntegerField(blank=True)),
                ('health', models.IntegerField(blank=True)),
                ('battle_cry', models.TextField(null=True)),
                ('death_rattle', models.TextField(null=True)),
                ('sorcery', models.TextField(null=True)),
            ],
        ),
    ]
