import os
import re

def rename_images_in_folder(path):
    files = os.listdir(path)
    for file in files: 
        new_file = re.sub(r'\([^)]*\)', '', file)
        new_file = new_file.replace(' ','')
        os.rename(os.path.join(path,file), os.path.join(path, new_file))
        print(new_file)

rename_images_in_folder('fulls')
rename_images_in_folder('thumbs')