import typing as ty


class Service:

    def __init__(
            self,
            name: str
    ) -> None:
        self.name = name

    def __call__(self, handle: callable) -> "Service":
        self.handle = handle
        return self

    async def get_proxy(self, proxy_type: str) -> ty.List[str]:
        return await self.handle(proxy_type)
