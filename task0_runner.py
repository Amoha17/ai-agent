
import asyncio
import aiohttp
from datetime import datetime

async def fetch_time():
    try:
        url = "http://worldtimeapi.org/api/timezone/Asia/Kolkata"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                data = await response.json()
                return f"[task0] Online time fetched: {data['datetime']}"
    except Exception as e:
        now = datetime.now().isoformat()
        return f"[task0] Offline fallback time: {now} (Reason: {str(e)})"

async def main():
    result = await fetch_time()
    print(result)
    with open("notes.md", "a") as f:
        f.write(f"\n{result}\n")

if __name__ == "__main__":
    asyncio.run(main())
