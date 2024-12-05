import asyncio,ctypes
async def alert(ctx, msg: str, title: str):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, ctypes.windll.user32.MessageBoxW, 0, msg, title, 0x30)