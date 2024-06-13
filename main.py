import asyncio

import aiohttp

from util import dreamMachineMake, refreshDreamMachine


async def main():
    # Your access_token
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOnsidXNlcl91dWlkIjoiNzE2YjJhMzItMDUwZS00ZmJmLWEyMjctMzIyMzgyZTUyNjM2IiwiY2xpZW50X2lkIjoiIn0sImV4cCI6MTcxODg2MTgwNn0.K2MG5LYabZYL5cyAsYDV1JqCMeWHqgyBdBTu9FHWBPI; refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOnsidXNlcl91dWlkIjoiNzE2YjJhMzItMDUwZS00ZmJmLWEyMjctMzIyMzgyZTUyNjM2IiwiY2xpZW50X2lkIjoiIn0sImV4cCI6MTcxODg2MTgwNn0.K2MG5LYabZYL5cyAsYDV1JqCMeWHqgyBdBTu9FHWBPI"
    prompt = "Pandas are fighting dinosaurs in space"
    make_json = dreamMachineMake(prompt, access_token)
    print(make_json)
    task_id = make_json[0]["id"]
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout) as session:

        while True:
            response_json = await refreshDreamMachine(session, access_token)

            for it in response_json:
                if it["id"] == task_id:
                    print("proceeding state " + it['state'])
                    if it['video']:
                        print(f"New video link: {it['video']['url']}")
                        return
                await asyncio.sleep(3)


if __name__ == "__main__":
    asyncio.run(main())
