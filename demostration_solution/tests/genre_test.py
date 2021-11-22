import pytest
from unittest.mock import MagicMock
import os

from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.model.genre import Genre
from demostration_solution.service.genre import GenreService
from demostration_solution.setup_db import db


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)
    genre_dao.get_all = MagicMock()
    genre_dao.get_one = MagicMock(return_value='Драма')
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre != None
        assert genre.id != None

    def test_get_all(self):
        genres= self.genre_service.get_all()
        assert  len(genres) > 0

    def create(self, genre_d):
        genre_d = {
            "name": "Документальный",
        }
        genre = self.genre_service.create(genre_d)
        assert genre.id != None

    def update(self):
        genre_d = {
            "id": 9,
            "name":"Комедия",
        }
        self.genre_service.update(genre_d)

    def partially_update(self, genre_d):
        genre = self.genre_service.get_one(genre_d["id"])
        if "name" in genre_d:
            genre.name = genre_d.get("name")
        self.genre_service.update(genre)

    def delete(self, rid):
        self.genre_service.delete(rid)


