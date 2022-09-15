#!/usr/bin/env python
# coding: utf-8

# ## Step 2
# From the Step 1 script create a file which allows the user to move only the file (given by input by the user).

# In[5]:


#start impoting libraries and modules
import numpy as np
from PIL import Image
import os
import shutil
import csv
import argparse

#creating the variable that shoul be called while running the scritp
parser = argparse.ArgumentParser()
parser.add_argument("file_to_move", type=str, help="This variable is the name of thhe file you want to move to the correct folder")
args = parser.parse_args()


    
el=args.file_to_move #associating the given file to the variable "el"
#checking if the given file name exists in the folder.
#If not a message is printed and the list of available files is given to the user to choose in
if el not in os.listdir():
    print("This file is not in the folder")
    print("Chose from:")
    print([f for f in os.listdir('.') if os.path.isfile(f)])
    #break
#from here I used the script of the step 1 with only little modifies in order to move only the selected file
    else:
    print("moving..")
    if "recap.csv" not in os.listdir():
        colonne=["name","type","size (B)"]
        recap = open("recap.csv", "w",newline='')
        writer=csv.writer(recap)
        writer.writerow(colonne)
        recap.close()
    else:
        pass
    
    #checking if file-type folders already exists. If not, creating them.
    folders=["documents","images","audios"]
    for fo in folders:
        try:
            os.makedirs(fo)    
        except FileExistsError:
            pass 

    recap = open("recap.csv", "a",newline='')
    writer=csv.writer(recap)

    if el.endswith("txt") or el.endswith("odt"):
        print(str(el).ljust(20) ,"type: doc".ljust(20), "size:"+ str(os.path.getsize(el))+"B".ljust(20))
        writer.writerow([(str(el)).split(".")[0] ,"document", str(os.path.getsize(el))])
        shutil.move( el, ".\documents\\" +el)
        
    elif el.endswith("png") or el.endswith("jpg") or el.endswith("jpeg"):
        print(str(el).ljust(20) ,"type: image".ljust(20), "size:"+ str(os.path.getsize(el))+"B".ljust(20))
        writer.writerow([(str(el)).split(".")[0] ,"image",  str(os.path.getsize(el))])
        shutil.move( el, ".\images\\" +el)
    
    elif el.endswith("mp3"):
        print(str(el).ljust(20) ,"type: audio".ljust(20), "size:"+ str(os.path.getsize(el))+"B".ljust(20))
        writer.writerow([(str(el)).split(".")[0] ,"audio",  str(os.path.getsize(el))])
        shutil.move( el, ".\\audios\\" +el)
    
    else:
        pass
    recap.close()




  

