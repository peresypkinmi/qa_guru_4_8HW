import csv
import os

from models.users import User


class UserProvider:
    def get_users(self) -> list[User]:
        raise NotImplementedError


class CsvUserProvider(UserProvider):
    csv_path: str

    def __init__(self, csv_path):
        assert os.path.exists(csv_path)
        self.csv_path = csv_path

    def get_users(self) -> list[User]:
        with open(self.csv_path, "r") as file:
            users = list(csv.DictReader(file, delimiter=";"))
        class_users = [User.from_csv_user(user) for user in users]
        return class_users


class ApiUserProvider(UserProvider):
    pass


class DatabaseUserProvider(UserProvider):
    pass
