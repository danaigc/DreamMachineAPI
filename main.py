import asyncio

from util import dreamMachineMake, refreshDreamMachine


async def main():
    # Your access_token
    access_token = ""
    prompt = "I flew to the roof"
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
