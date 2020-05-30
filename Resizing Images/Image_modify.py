"""

Function to parse a folder and resize all the images inside each folder
writing the resultant files into a  new directory called test directory


"""

import cv2
import os
from Fill import *
import pandas as pd
from PIL import Image
from matplotlib import *
import numpy as np

#################################

##################################

def load_images_from_folder(folder,i):
    base_destination ='E:\\Work\\Project\\Reading images\\testDir\\'

    destination = base_destination + str(i)
    if not os.path.exists(destination):
        os.makedirs(destination)

    #cv2.namedWindow("gray", cv2.WINDOW_NORMAL);
    #cv2.namedWindow("cropped", cv2.WINDOW_NORMAL);
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        gray = cv2.cvtColor(np.float32(img), cv2.COLOR_BGR2GRAY)

        #cv2.imshow("gray", gray)
        #cv2.waitKey(0)
        # cv2.destroyAllWindows()
        if gray is not None:
            if gray.size != 0:
                df = fill(gray)
                df = numpy.asarray(df, dtype=np.uint8)

                #cv2.imshow("cropped", df)
                #cv2.waitKey(0)

                print('checkpoint 1', destination + '\\' + filename)
                cv2.imwrite(destination + '\\' + filename, df)
                print('checkpoint 2')


for i in range(0,62):
    folder_name = "E:\\Work\\Project\\Reading images\\res imgs\\" + str(i)
    load_images_from_folder(folder_name,i)
