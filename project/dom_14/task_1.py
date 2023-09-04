# На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.
from pathlib import Path

import pytest
from spam import User, Project, AccessError, LevelError


@pytest.fixture
def new_set():
    data = {
        User(name='Admin', id=999, level=1),
        User(name='user', id=246, level=3),
        User(name='Neo', id=5, level=6),
    }
    return data


@pytest.fixture
def good_user():
    return User(name='user', id=123, level=3)


@pytest.fixture
def new_user():
    return User(name='new', id=89, level=3)


def test_load(new_set):
    project = Project()
    result = project.load_users_from_json()
    assert result == new_set


def test_enter(good_user):
    project = Project()
    project.load_users_from_json()
    result = project.login('user', 246)
    assert result == good_user


def test_no_enter():
    project = Project()
    project.load_users_from_json()
    with pytest.raises(AccessError):
        project.login('ertdh', 245)


def test_add_user(new_user):
    project = Project()
    project.load_users_from_json()
    project.login('user', 345)
    result = project.add_user('name', 34567, 7)
    assert new_user == result



if __name__ == '__main__':
    pytest.main(['-vv'])
