from django.urls import path
from .views import FilmList, FilmDetail, GenreList, GenreDetail, LanguageList, LanguageDetail, CountryList, CountryDetail
urlpatterns = [
    path('films/', FilmList.as_view(), name='film-list'),
    path('films/<int:pk>/', FilmDetail.as_view(), name='film-detail'),
    path('genres/', GenreList.as_view(), name='genre-list'),
    path('genres/<int:pk>/', GenreDetail.as_view(), name='genre-detail'),
    path('countries/', CountryList.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryDetail.as_view(), name='country-detail'),
    path('languages/', LanguageList.as_view(), name='language-list'),
    path('languages/<int:pk>/', LanguageDetail.as_view(), name='language-detail')
]
