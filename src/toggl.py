from datetime import datetime
from base64 import b64encode
import asyncio

import httpx

from settings import TOGGL_API_KEY
from schemas import WorkDayDuration


async def fetch_working_days() -> :
    async with httpx.AsyncClient(
            base_url="https://api.track.toggl.com/api/v9",
            headers={
                "content-type": "application/json",
                'Authorization': f"Basic {b64encode(f'{TOGGL_API_KEY}:api_token'.encode()).decode('ascii')}"
            }
    ) as client:
        response = await client.get("/me/time_entries")
        data = response.json()
        days = [
            WorkDayDuration(
                at=datetime.fromisoformat(item["at"]),
                project_name=item["description"],
                duration=item["duration"],
            )
            for item in data
        ]


if __name__ == "__main__":
    asyncio.run(fetch_working_days())



