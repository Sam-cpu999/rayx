import ctypes, sys, os, random, string, time
def ensure_admin_and_check_ran(log_file):
    if not os.path.exists(log_file):
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
            time.sleep(0.1)
            if not ctypes.windll.shell32.IsUserAnAdmin():
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
        with open(log_file, "w") as f:
            f.write(''.join(random.choices(string.ascii_letters + string.digits, k=50)))