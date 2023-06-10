from dataclasses import dataclass

from tables import User
from repositories.base import BaseRepo
from repositories.mixins import CreateMixin, TestMixin, GetMixin


@dataclass
class UserRepo(BaseRepo, CreateMixin, GetMixin, TestMixin):
    table = User
