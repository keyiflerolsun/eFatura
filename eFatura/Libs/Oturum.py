# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, urllib3, ssl
from typing import Any

class CustomHttpAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, ssl_context: ssl.SSLContext | None = None, **kwargs: Any) -> None:
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections: int, maxsize: int, block: bool = False, **kwargs: Any) -> None:
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools   = connections,
            maxsize     = maxsize,
            block       = block,
            ssl_context = self.ssl_context,
            **kwargs,
        )

def legacy_session() -> requests.Session:
    """Eski SSL sunucu bağlantı ayarlarını içeren istek oturumu oluşturur."""
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= getattr(ssl, "OP_LEGACY_SERVER_CONNECT", 0x4)

    session = requests.Session()
    session.mount("https://", CustomHttpAdapter(ctx))
    return session
