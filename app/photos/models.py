from random import randint

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Photo(models.Model):

    image_name = models.CharField(
        "Наименование файла",
        max_length=50,
    )
    file = models.ImageField(
        "Файл",
        upload_to="images/",
    )
    random_int = models.IntegerField(
        "Рандомное значение",
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        default=randint(1, 1000),
    )
    load_time = models.DateTimeField(
        "Время сохранения",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ("-id",)

    def __str__(self):
        return self.image_name
