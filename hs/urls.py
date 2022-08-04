from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('hs/<int:card_id>/', views.show_card, name='show_card'),
]