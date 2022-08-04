from django.http import HttpResponseNotFound
from .models import Card
from django.shortcuts import render, redirect


def index(request):
    cards = Card.objects.all()
    return render(request, 'hs/index.html',
                  {'title': 'Hearthstone Battleground Cards',
                   'cards': cards})


def show_card(request, card_id):

    try:
        card = Card.objects.filter(pk=card_id)[0]

        return render(request, 'hs/card.html',
                  {'title': card.name,
                   'card': card})
    except:
        pageNotFound(request, Exception('out of range'))




def pageNotFound(request, exception):
    return redirect('home')
