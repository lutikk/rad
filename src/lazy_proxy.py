import asyncio
import typing as ty

from src.proxy_checker import ProxyChecker
from src.proxy_grabber import ProxyGrabber
from src.services import __services__


class LazyProxy:

    def __init__(self, proxy_type: str):
        self.grabber = ProxyGrabber(__services__)
        self.checker = ProxyChecker()
        self.proxy_type = proxy_type

    async def _get_proxies(self) -> ty.List[str]:
        proxies = await self.grabber.get(self.proxy_type)
        proxies = await self.checker.check_proxies(proxies)
        return proxies

    def get_proxies(self, file_name: str) -> None:
        proxies = asyncio.run(self._get_proxies())
        file = open(file_name, "w")
        file.writelines(proxies)
