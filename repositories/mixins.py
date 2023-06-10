import typing
from dataclasses import dataclass

from sqlalchemy import Engine, select
from sqlalchemy.orm import sessionmaker


@dataclass
class BaseMixin:
    table: typing.Any
    engine: Engine
    session_maker: sessionmaker


@dataclass
class CreateMixin(BaseMixin):

    def create(self, **kwargs):
        with self.session_maker() as session:
            instance = self.table(**kwargs)
            session.add(instance)
            session.commit()
            session.refresh(instance)
        return instance


@dataclass
class GetMixin(BaseMixin):
    def get_first_by_values(self, **kwargs):
        with self.session_maker() as session:
            query = select(self.table).filter_by(**kwargs)

            instance = session.execute(query).first()
            return instance



@dataclass
class TestMixin(BaseMixin):

    def test_m(self):
        with self.session_maker() as session:
            query = select(self.table).filter_by(login='ggg')

            instance = session.execute(query).first()
            return instance

# @dataclass
# class GetMixin(BaseMixin):
#
#     def get_by_id(self):
#         query = self.table.get(10)
