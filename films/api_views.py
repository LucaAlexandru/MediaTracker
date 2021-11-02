from rest_framework import viewsets
from films.models import Film
from films.api_serializers import FilmSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer