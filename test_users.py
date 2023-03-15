
import csv

import pytest

# -------------------------------------------------------------------
# Прямолинейный вариант теста
# -------------------------------------------------------------------


def test_workers_are_adults():
    file = open("users.csv")
    users = csv.DictReader(file, delimiter=";")
    workers = [user for user in users if user["status"] == "worker"]
    for worker in workers:
        assert int(worker["age"]) >= 18
    file.close()

# -------------------------------------------------------------------
# Улучшаем код
# -------------------------------------------------------------------


@pytest.fixture
def users():
    with open("users.csv") as file:
        users = csv.DictReader(file, delimiter=";")
        users = [user for user in users]
    return users


@pytest.fixture
def workers(users):
    workers = [user for user in users if user["status"] == "worker"]
    return workers


def test_workers_are_adults_v2(workers):
    for worker in workers:
        assert int(worker["age"]) >= 18


# -------------------------------------------------------------------
# Используем объектный подход работы с данными
# -------------------------------------------------------------------
