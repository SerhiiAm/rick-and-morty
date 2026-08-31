from django.urls import path
from characters.views import get_random_character_view, CharacterListView

app_name = "characters"
urlpatterns = [
    path("character/random/", get_random_character_view, name="character-random"),
    path("character/", CharacterListView.as_view(), name="character-list"),
]
