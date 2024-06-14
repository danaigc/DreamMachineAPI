import asyncio

from util import dreamMachineMake, refreshDreamMachine


async def main():
    # Your access_token
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOnsidXNlcl91dWlkIjoiYjY1ZTdjMWYtYTExYi00ZjI4LWE0NjYtNTk5N2YxOTBjMWI2IiwiY2xpZW50X2lkIjoiIn0sImV4cCI6MTcxODg4OTQwMn0.Yx_0KXpPfIc7i33XSZ6B2HVuqbNY1dIbau6YkII_0as"
    prompt = "They grew wings and flew"
    # The image path can be empty
    img_file = ""
    # img_file = "img/meinv.png"

    make_json = dreamMachineMake(prompt, access_token, img_file)
    print(make_json)
    task_id = make_json[0]["id"]
    while True:
        response_json = refreshDreamMachine(access_token)

        for it in response_json:
            if it["id"] == task_id:
                print(f"proceeding state {it['state']}")
                if it['video']:
                    print(f"New video link: {it['video']['url']}")
                    return
            await asyncio.sleep(3)


if __name__ == "__main__":
    asyncio.run(main())
