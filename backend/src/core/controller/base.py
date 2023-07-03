from typing import Any, Generic, List, TypeVar, Union, get_args

from core.database.session import Base
from core.repository.base import BaseRepository

ModelType = TypeVar('ModelType', bound=Base)


class BaseController(Generic[ModelType]):

    def __init__(self, repository: BaseRepository):
        self.model = get_args(self.__class__.__orig_bases__[0])[0]
        self.repository = repository

    async def get_all(
        self, skip: int = 0, limit: int = 5, join: Union[set[str], None] = None,  # noqa: WPS221
    ) -> List[ModelType]:
        return await self.repository.get_all(skip, limit, join)

    async def create(self, data: dict[str, Any]) -> Union[ModelType, None]:
        item = await self.repository.create(data)
        await self.repository.apply_changes()
        return item

    async def search(self, attributes: dict, limit: int) -> Union[List[ModelType], None]:
        return await self.repository.search(attributes, limit)
