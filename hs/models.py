import os.path

from django.conf import settings
from django.db import models


def images_path():
    return os.path.join(settings.STATIC_URL, '\\hs\\images\\minions\\')


class Archetype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15, verbose_name='Название архетипа')

    class Meta:
        verbose_name = 'название архетипа'
        verbose_name_plural = 'Архетипы'

    def __str__(self):
        return self.name


class Feature(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=20, verbose_name='Способность')
    feature_disc = models.CharField(max_length=50, verbose_name='Краткое описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'название способности'
        verbose_name_plural = 'Способности'


class Card(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30, blank=True, verbose_name='Название карты')
    image = models.FilePathField(path=images_path, blank=True, verbose_name='Ссылка на картинку')
    card_about = models.CharField(max_length=150, blank=True, verbose_name='Описание карты')
    archetype = models.ForeignKey(Archetype, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Архетип')
    attack = models.IntegerField(blank=True, verbose_name='Атака')
    health = models.IntegerField(blank=True, verbose_name='Здоровье')
    tavern_level = models.IntegerField(default=1, blank=True, verbose_name='Уровень таверны')
    has_features = models.BooleanField(verbose_name='Способности', default=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'название карты'
        verbose_name_plural = 'Карты'


class CardFeature(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, verbose_name='Карта', default='',
                             limit_choices_to={'has_features': 1})
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, verbose_name='Свойство', default='')

    def __str__(self):
        return f"Пара {self.card.name} - {self.feature.name}"

    class Meta:
        verbose_name = 'способности карт'
        verbose_name_plural = 'Способности карт'
