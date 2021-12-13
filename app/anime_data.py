from typing import Any, Dict
import asyncio
from jikanpy import AioJikan, Jikan

jikan = Jikan()


def get_anime():
    sn = jikan.season()
    data = sn.get('anime')
    print("Here")
    # print(data)
    return data


"""
async def main() -> Any:
    async with AioJikan() as aiojikan:
        latest_season: Any = await aiojikan.season()
        print(latest_season.get('anime')[0])
        print("here")
        return await latest_season


# asyncio.run(main())
# fn = main()
loop = asyncio.get_event_loop()


async def get_anime():
    fn = asyncio.run(main())
    t1 = main()
    await fn
    print(t1)
    return await t1

m = asyncio.wait(get_anime())
print(m)"""
