import asyncio

import aiohttp

from util import dreamMachineMake, refreshDreamMachine


async def main():
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOnsidXNlcl91dWlkIjoiYWE2MzVkY2EtMWU0NC00YjFiLTk1YTItOWEyYjA1ZWY3NTAxIiwiY2xpZW50X2lkIjoiIn0sImV4cCI6MTcxODg1Mjk4MX0.QdmkCSJ0NTvU-l2_vfhuNAAiYJpNPfurXcC6R36435A"
    # 这里替换成您的access_token
    prompt = "Little pigs are running on the grass"
    dreamMachineMake(prompt, access_token)


    async with aiohttp.ClientSession() as session:
        previous_ids = set()
        while True:
            response_json = await refreshDreamMachine(session, access_token)
            item = response_json[0]
            if item['id'] not in previous_ids and item['state'] == 'completed':
                previous_ids.add(item['id'])
                if item['video']:
                    print(f"New video link: {item['video']['url']}")
                    break
            await asyncio.sleep(3)



if __name__ == "__main__":
    asyncio.run(main())
