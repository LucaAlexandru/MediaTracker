from rest_framework import viewsets
from games.models import Game
from games.api_serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer