import os
import shutil

def Move_File(path_to_file, path_to_new):
    shutil.move(path_to_file, path_to_new)


directory = os. getcwd() + "/U"


for filename in os.listdir(directory):

    if filename.endswith(".jpg"):
        image_name = filename.replace(" ", "").replace(".jpg","")
        newpath = directory + "/" + image_name
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        
        Move_File(directory + "/" + filename, newpath)


    else:
        continue