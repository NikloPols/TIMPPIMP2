import asyncio
from create_bot import dp, bot
from handlers import privet, on_help, echo, on_startup



if __name__ == '__main__':

    from aiogram import executor
    loop = asyncio.get_event_loop()
    loop.create_task(executor.start_polling(dp, on_startup=on_startup))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.stop()
        loop.close()
