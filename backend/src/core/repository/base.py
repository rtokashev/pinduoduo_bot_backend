import logging
from functools import reduce
from typing import Any, Generic, List, TypeVar, Union, get_args

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import and_, select

from core.database.session import Base

ModelType = TypeVar('ModelType', bound=Base)


class BaseRepository(Generic[ModelType]):  # noqa: WPS214

    def __init__(self, db_session: AsyncSession):
        self.model = get_args(self.__class__.__orig_bases__[0])[0]
        self.db_session = db_session

    async def create(self, data: dict[str, Any] = None) -> Union[ModelType, None]:
        if data is None:
            data = {}
        model = self.model(**data)
        self.db_session.add(model)
        try:
            await self.db_session.commit()
        except Exception as err:
            await self.db_session.rollback()
            logging.error(str(err))
            raise err
        return model

    async def search(self, attributes: dict, limit: int) -> Union[List[ModelType], None]:
        query = await self._query()
        conditions = [
            getattr(self.model, attribute) == attributes[attribute] for attribute in attributes
        ]
        query = query.filter(and_(*conditions)).limit(limit)
        result_set = await self.db_session.scalars(query)
        return result_set.all()

    async def delete(self, data: dict[str, Any]) -> None:
        await self.db_session.delete(self.model(**data))

    async def get_all(
        self, skip: int = 0, limit: int = 5, join: Union[set[str], None] = None,  # noqa: WPS221
    ) -> List[ModelType]:
        query = await self._query(join)
        query = query.offset(skip).limit(limit)
        return await self._all(query)

    def _add_join_to_query(self, query: Select, join: str) -> Select:
        return getattr(self, ''.join(['_join_', join]))(query)

    async def _join(self, query: Select, join: set[str]) -> Select:
        return reduce(self._add_join_to_query, join, query)

    async def _query(
        self, join: Union[set[str], None] = None, order: Union[dict, None] = None,  # noqa: WPS221
    ) -> Select:
        # В случае необходимости можно добавить join
        query = select(self.model)
        return await self._join(query, join) if join else query

    async def _all(self, query: Select) -> List[ModelType]:
        result_set = await self.db_session.scalars(query)
        return result_set.all()

    async def _first(self, query: Select) -> Union[ModelType, None]:
        result_set = await self.db_session.scalars(query)
        return result_set.first()

    async def _one_or_none(self, query: Select) -> Union[ModelType, None]:
        result_set = await self.db_session.scalars(query)
        return result_set.one_or_none()

    async def _one(self, query: Select) -> Union[ModelType, None]:
        result_set = await self.db_session.scalars(query)
        return result_set.one()
