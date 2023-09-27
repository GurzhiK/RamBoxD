from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.ManyToManyField(Genre, related_name='films')
    runtime_minutes = models.CharField(max_length=15)
    poster = models.ImageField(upload_to='film_posters/')
    trailer_url = models.URLField(blank=True, null=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='films')
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, related_name='films')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title
