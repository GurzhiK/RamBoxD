from rest_framework import serializers
from .models import Genre, Country, Language, Film


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    genre = serializers.StringRelatedField()
    language = serializers.StringRelatedField()
    genre = GenreSerializer(many=True)

    class Meta:
        model = Film
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'
