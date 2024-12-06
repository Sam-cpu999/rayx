import ctypes, sys, time
def ensure_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return
    while True:
        result = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
        if result <= 32:
            time.sleep(0.1)
        else:
            return
