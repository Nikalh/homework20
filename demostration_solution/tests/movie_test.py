import pytest
from unittest.mock import MagicMock
import os

from demostration_solution.dao.model.movie import Movie
from demostration_solution.dao.movie import MovieDAO
from demostration_solution.service.movie import MovieService
from demostration_solution.setup_db import db


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)
    movie_dao.get_all = MagicMock()
    movie_dao.get_one = MagicMock(return_value='Драма')
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

class TestGenreService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie != None
        assert movie.id != None

    def test_get_all(self):
        movie= self.movie_service.get_all()
        assert  len(movie) > 0

    def create(self, movie_d):
        movie_d = {
            "name": "Документальный",
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id != None

    def update(self):
        movie_d = {
            "id": 9,
            "name":"Комедия",
        }
        self.movie_service.update(movie_d)

    def partially_update(self, movie_d):
        movie = self.movie_service.get_one(movie_d["id"])
        if "name" in movie_d:
            movie.name = movie_d.get("name")
        self.movie_service.update(movie)

    def delete(self, rid):
        self.movie_service.delete(rid)
