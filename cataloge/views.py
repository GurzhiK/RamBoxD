from django.shortcuts import render
from .models import Film, Language, Country, Genre
from .serializers import GenreSerializer, CountrySerializer, LanguageSerializer, FilmSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class FilmList(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = [filters.OrderingFilter,
                       DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']
    filterset_fields = ['genre', 'country', 'language']
    ordering_fields = ['title', 'id', 'genre', 'country', 'language']
    ordering = ['title', 'id', 'genre', 'country', 'language']


class FilmDetail(generics.RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class LanguageList(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageDetail(generics.RetrieveAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetail(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
