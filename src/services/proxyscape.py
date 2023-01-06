import typing as ty

import aiohttp

from src.service import Service


@Service("proxyscape")
async def proxyscape_grabber(proxy_type: str) -> ty.List[str]:
    data = {
        "request": "getproxies",
        "proxytype": proxy_type,
        "timeout": 10000,
        "country": "all",
        "ssl": "all",
        "anonymity": "all"
    }
    proxies = []
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.proxyscrape.com", params=data) as response:
            proxies.extend((await response.read()).decode("utf-8").split("\n"))
    return list(filter(None, proxies))
