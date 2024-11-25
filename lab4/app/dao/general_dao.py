from abc import ABC
from typing import List

from sqlalchemy import inspect
from sqlalchemy.orm import Mapper

from app import db


class GeneralDAO(ABC):

    _domain_type = None
    _session = db.session

    def find_all(self) -> List[object]:
        # Повертає всі записи в базі даних для цього типу
        return self._session.query(self._domain_type).all()

    def find_by_id(self, key: int) -> object:
        # Знаходить об’єкт за його ключем
        return self._session.query(self._domain_type).get(key)

    def create(self, obj: object) -> object:
        # Додає новий об’єкт у базу даних
        self._session.add(obj)
        self._session.commit()
        return obj

    def create_all(self, obj_list: List[object]) -> List[object]:
        # Додає кілька нових об’єктів у базу даних
        self._session.add_all(obj_list)
        self._session.commit()
        return obj_list

    def update(self, key: int, in_obj: object) -> None:
        # Оновлює наявний об’єкт за заданим ключем
        domain_obj = self._session.query(self._domain_type).get(key)
        mapper: Mapper = inspect(type(in_obj))
        columns = mapper.columns._collection
        for column_name, column_obj, *_ in columns:
            if not column_obj.primary_key:
                value = getattr(in_obj, column_name)
                setattr(domain_obj, column_name, value)
        self._session.commit()

    def patch(self, key: int, field_name: str, value: object) -> None:
        # Змінює конкретне поле об’єкта за заданим ключем
        domain_obj = self._session.query(self._domain_type).get(key)
        setattr(domain_obj, field_name, value)
        self._session.commit()

    def delete(self, key: int) -> None:
        # Видаляє об’єкт за заданим ключем
        domain_obj = self._session.query(self._domain_type).get(key)
        self._session.delete(domain_obj)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise

    def delete_all(self) -> None:
        # Видаляє всі об’єкти цього типу
        self._session.query(self._domain_type).delete()
        self._session.commit()
