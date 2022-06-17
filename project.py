import os
import shutil
import time

def remove_files(path):
    path_time = os.stat(path).st_ctime
    time_period = 30*24*60*60
    now = time.time()

    if int(now - path_time) > time_period:
        if os.path.isfile(path):
            os.remove(path)
            print("File ", path, " removed")
        elif os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
            print("Folder ", path, " removed")
        return 1


user_input = input("Enter directory name to be sorted ")

if os.path.exists(user_input):

    for (root, dirs, files) in os.walk(user_input, topdown = True):

        run = remove_files(root)

        if run == 1:
            print("Folder sorted")
            quit()
        else:
            if files:
                for file in files:
                    if file == '.DS_Store':
                        continue
                    else: 
                        path = os.path.join(root, file)
                        remove_files(path)
    
    print("Folder sorted")

else: 
    print("Path does not exist. Please enter a different path")