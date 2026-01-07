from api.controllers.user_controller import create_user
from repository.user_repository import UserRepository
from tests.helper.user_factory import create_user


def test_save_user(db):
    repo = UserRepository()

    user = create_user()
    saved = repo.save(db, user)

    assert saved.id is not None



def test_find_by_username(db):
    repo = UserRepository()

    repo.save(db, create_user(username="rene"))

    found = repo.find_by_username(db, "rene")

    assert found.username == "rene"



def test_find_all(db):
    repo = UserRepository()

    repo.save(db, create_user(username="rene"))
    repo.save(db, create_user(username="ana", email="ana@test.com"))

    users = repo.find_all(db)

    assert len(users) == 2


