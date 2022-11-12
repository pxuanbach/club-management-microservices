import aiohttp
import json

from schemas import EventData


async def send_event(url, event_type, data):
    url = url + "/api/v1/events"
    send_data = EventData(
        type=event_type,
        data=json.dumps(data)
    )
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.post(url, json=send_data.dict()) as resp:
            print(resp.status)
            print(await resp.text())
