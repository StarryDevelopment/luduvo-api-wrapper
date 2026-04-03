from typing import Callable, Awaitable, List, TypeVar

T = TypeVar("T")


class Pagination:
    def __init__(
        self,
        fetch_page: Callable[[int, int], Awaitable[dict]],
        limit: int = 50,
    ):
        self._fetch_page = fetch_page
        self.limit = limit

    async def all(self) -> List[T]:
        offset = 0
        results: List[T] = []

        while True:
            data = await self._fetch_page(self.limit, offset)

            items = data["items"]
            total = data["total"]

            results.extend(items)

            offset += self.limit

            if offset >= total or not items:
                break

        return results
