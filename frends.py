import asyncio

from pydantic import ValidationError
from vkbottle import VKError
from vkbottle.api import API


class NewFollowersGenerator:

    def __init__(self, api: API):
        self.__api = api
        self.__count = 1
        self.__offset = 0
        self.  offset = 0

    async def __aiter__(self):
        while self.__offset < self.__count:

            try:
                followers = await self.__api.request(
                    'friends.getRequests',
                    dict(
                        offset=self.__offset,
                        count=1000,
                        sort=1,
                        need_viewed=0
                    ),
                    raw_response=True
                )
            except VKError as ex:
                await asyncio.sleep(5)
                followers = await self.__api.request(
                    'friends.getRequests',
                    dict(
                        offset=self.__offset,
                        count=1000,
                        sort=1,
                        need_viewed=0
                    ),
                    raw_response=True
                )
            except ValidationError:
                followers = None

            if not followers:
                self.__offset += 1000
                continue

            self.__count = followers['count']
            for follower in followers['items']:
                yield follower
            self.__offset += 1000
