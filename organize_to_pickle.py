"""

Function to parse a folder and organise data for pickling
store the resultant data into a image_dictionary array, ready for pickling
Then pickle the file using pickle.dumb and saving the output file to image_dict

"""

import cv2
import os
import numpy as np
import pickle


#################################

def load_images_from_folder(folder, i):
    i = []

    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))  # Reading files from folders
        gray = cv2.cvtColor(np.float32(img), cv2.COLOR_BGR2GRAY)  # Converting to gray so that num of channels is 1

        i.append(gray)  # Appending to array

    # print(np.array(i).shape)
    return np.array(i).astype('int')


##########################################

# full_set =[]
image_dict = {}

for i in range(0, 62):
    folder_name = "E:\\Work\\Project\\Reading images\\testDir\\" + str(i)        # Change to local folder location
    # full_set.append(load_images_from_folder(folder_name, i))					# Creating a list of items of images arrays

    image_dict[i] = load_images_from_folder(folder_name, i)  # Creating dictionary of filename : array of images

    print(image_dict)

outfile = open('image_pickle', 'wb')  # Giving writing permission and biniary file
pickle.dump(image_dict, outfile)  # Pickle the file and generating output
outfile.close()
