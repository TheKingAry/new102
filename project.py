import os
import shutil
source=r"C:\Users\ZEBRONICS01\Downloads\C102_assets-main"
destination=r"C:\Users\ZEBRONICS01\Downloads\C102_assets-main\documents"
list_of_files = os.listdir(source)

for files in list_of_files:
    name,extension=os.path.splitext(files)
    if extension == "":
        continue
    if extension in [".pdf",".ppt",".txt"]:
        path1= source+"/"+files
        path2=destination
        path3=path2+"/"+files
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)