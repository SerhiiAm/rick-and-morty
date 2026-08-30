from django.db import models


class Character(models.Model):

    class CharacterStatus(models.TextChoices):
        ALIVE = "Alive"
        DEAD = "Dead"
        UNKNOWN = "unknown"

    class GenderStatus(models.TextChoices):
        FEMALE = "Female"
        MALE = "Male"
        Genderless = "Genderless"
        UNKNOWN = "unknown"

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50,
        choices=CharacterStatus.choices,
        default=CharacterStatus.UNKNOWN,
    )
    species = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=50,
        choices=GenderStatus.choices,
    )
    image = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.name
