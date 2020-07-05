"""

Function to parse a folder and organise data for pickling
creating cross pickling set
"""

import cv2
import os
import numpy as np
import pickle



#################################

def load_images_from_folder(folder, i):



    #cv2.namedWindow("gray", cv2.WINDOW_NORMAL);
    #cv2.namedWindow("cropped", cv2.WINDOW_NORMAL);

    i = []
    count = 0
    for filename in os.listdir(folder):
        if count <= 10:
            img = cv2.imread(os.path.join(folder, filename))						# Reading files from folders
            gray = cv2.cvtColor(np.float32(img), cv2.COLOR_BGR2GRAY)		        # Converting to gray so that num of channels is 1

            i.append (gray)															# Appending to array
            count++
        else:

            return np.array(i).astype('int')
##########################################

#full_set =[]
cross_dict = {}

for i in range(0,62):
    folder_name = "E:\\Work\\Project\\Reading images\\testDir\\" + str(i)       # Change to local folder location
    #full_set.append(load_images_from_folder(folder_name, i))					# Creating a list of items of images arrays
    cross_dict[i] = load_images_from_folder(folder_name, i)						# Creating dictionary of filename : array of images
    #len(full_set)
    #print(image_dict)

outfile = open('cross_pickle','wb')                                             # Giving writing permission and biniary file
pickle.dump( cross_dict,outfile)                                                # Pickle the file and generating output
outfile.close()