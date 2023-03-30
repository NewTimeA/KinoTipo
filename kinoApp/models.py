from django.db import models
from pytils.translit import slugify

class Genres(models.Model):
    genreName = models.CharField("Жанр", max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return self.genreName

    def save(self, *args, **kwargs):
        self.slug = slugify(self.genreName)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Movie(models.Model):
    movieName = models.CharField("Наименование фильма", max_length=255, null=True, blank=True)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE, verbose_name="Жанр")
    year = models.IntegerField("Год", null=True, blank=True)
    country = models.CharField("Страна", max_length=255, null=True, blank=True)
    producer = models.CharField("Продюссер", max_length=255, null=True, blank=True)
    description = models.TextField("Описание", null=True, blank=True)
    cover = models.CharField("Обои", max_length=500, null=True, blank=True)
    poster = models.CharField("Постер", max_length=500, null=True, blank=True)
    movieLink = models.CharField("Ссылка на фильм", max_length=500, null=True, blank=True)
    isRec = models.BooleanField("Рекомендовано", null=True, blank=True)
    isTop = models.BooleanField("Топ-10", null=True, blank=True)
    rating = models.FloatField("Рейтинг", null=True, blank=True)

    def __str__(self):
        return self.movieName

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"