# Generated by Django 4.0.6 on 2022-08-01 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hs', '0007_alter_archetype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='archetype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hs.archetype'),
        ),
    ]
