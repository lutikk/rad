from src.lazy_proxy import LazyProxy

proxy = LazyProxy("http")
proxy.get_proxies("proxies.txt")


