import requests

from django.conf import settings
from characters.models import Character


def scraper_character() -> list[Character]:
    next_page_url = settings.RICK_AND_MORTY_API_CHARACTERS_URL
    characters = []

    while next_page_url is not None:
        character_response = requests.get(next_page_url).json()

        for character_dict in character_response["results"]:
            characters.append(
                Character(
                    api_id=character_dict["id"],
                    name=character_dict["name"],
                    status=character_dict["status"],
                    species=character_dict["species"],
                    gender=character_dict["gender"],
                    image=character_dict["image"],
                )
            )

        next_page_url = character_response["info"]["next"]

    return characters


def save_characters(characters: list[Character]) -> None:
    Character.objects.bulk_create(
        characters,
        update_conflicts=True,
        unique_fields=["api_id"],
        update_fields=["name", "status", "species", "gender", "image"],
    )


def sync_characters_with_api() -> None:
    characters = scraper_character()
    save_characters(characters)
