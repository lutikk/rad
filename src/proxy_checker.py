import asyncio
import typing as ty
from loguru import logger as log
from src.utils import chunks


class ProxyChecker:

    def __init__(self):
        self.counter = 0

    async def check_proxy(self, proxy: str) -> ty.Optional[str]:
        try:
            check = await asyncio.create_subprocess_exec(
                'ping', '-w', '1', proxy.split(":")[0],
                stdout=asyncio.subprocess.PIPE
            )
            out, error = await check.communicate()
            self.counter += 1
            if not error:
                log.success(f"[{self.counter}][GOOD] {proxy}")
                return proxy
        except Exception:
            self.counter += 1
        finally:
            log.error(f"[{self.counter}][BAD] {proxy}")
            pass

    async def check_proxies(self, proxies: ty.List[str]) -> ty.List[str]:
        checked_proxies = []
        for proxies_chunked in chunks(proxies, 100):
            results = await asyncio.gather(*[
                self.check_proxy(proxy)
                for proxy in proxies_chunked
            ])
            checked_proxies.extend(list(filter(None, results)))
        return checked_proxies
