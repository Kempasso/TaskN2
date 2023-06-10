from dataclasses import dataclass

from repositories.base import BaseRepo
from repositories.mixins import CreateMixin, GetMixin
from tables.files import Files


@dataclass
class FilesRepo(BaseRepo, CreateMixin, GetMixin):
    table = Files
