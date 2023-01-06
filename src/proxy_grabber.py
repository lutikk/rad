import asyncio
import typing as ty

from src.service import Service


class ProxyGrabber:

    def __init__(self, services: ty.List[Service]):
        self.services = services

    async def get(self, proxy_type: str) -> ty.List[str]:
        results = await asyncio.gather(*[
            service.get_proxy(proxy_type)
            for service in self.services
        ])
        proxies = []
        for result in results:
            proxies.extend(result)
        return proxies
