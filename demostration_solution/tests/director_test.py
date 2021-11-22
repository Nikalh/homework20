import pytest
from unittest.mock import MagicMock

import os

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.service.director import DirectorService
from demostration_solution.setup_db import db


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)
    director_dao.get_all = MagicMock()
    director_dao.get_one = MagicMock(return_value='Драма')
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director != None
        assert director.id != None

    def test_get_all(self):
        directors= self.director_service.get_all()
        assert  len(directors) > 0

    def create(self, director_d):
        director_d = {
            "name": "Документальный",
        }
        director = self.director_service.create(director_d)
        assert director.id != None

    def update(self):
        director_d = {
            "id": 9,
            "name":"Комедия",
        }
        self.director_service.update(director_d)

    def partially_update(self, director_d):
        director = self.director_service.get_one(director_d["id"])
        if "name" in director_d:
            director.name = director_d.get("name")
        self.director_service.update(director)

    def delete(self, rid):
        self.director_service.delete(rid)
