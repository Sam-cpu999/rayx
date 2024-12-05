import os,ctypes,requests
def change_wallpaper():
 try:
  file_path=os.path.join(os.path.expanduser('~'),"wallpaper_temp.png")
  with open(file_path,'wb')as f:f.write(requests.get("https://i.ibb.co/gD80MYf/imageonline-co-textimage.png").content)
  ctypes.windll.user32.SystemParametersInfoW(20,0,file_path,3)
  ctypes.windll.user32.SystemParametersInfoW(20,0,file_path,0x02)
 except Exception as e:print(f"Error changing wallpaper: {e}")