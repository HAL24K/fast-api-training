import httpx

from models.location import Location


async def get_live_report(location: Location):
    url = f'https://weather.talkpython.fm/api/weather?city={location.city}&country={location.country}&units=imperial'
    if location.state:
        url += f'&state={location.state}'

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

        data = resp.json()

    return data