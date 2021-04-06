import random
import cv2
import pyodbc
import pandas as pd
import re
import autoit ## pip install pyautoit
import time
import tkinter as tk
import os
import numpy as np
from tkinter import filedialog
from tkinter import messagebox

# autoit.win_active('Pick Place for 74380B - Excel')
# autoit.win_move('Pick Place for 74380B - Excel',0,0)

HEADER = ["REF", "PART_NUM", "X", "Y","ROTATION"]  #Adding a note to see if this fixes the push notifications


USERNAME = os.getlogin()

FILE_PATHS = [os.path.join(os.path.join(r'C:\Users',USERNAME),'Desktop\ZFirst'), os.path.join(os.path.join(r'C:\Users',USERNAME),'Desktop\ZFirst')]


def openfiledialog(starting_dir):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir=starting_dir) #Centroid first, then image file
    if file_path:
        return file_path
    else:
        exit()

# im_gray = cv2.imread(openfiledialog(starting_dir=r'C:\Users\rburns\Desktop\ZFirst'), cv2.IMREAD_GRAYSCALE) #r'C:\Users\rburns\Desktop\ZFirst\BPE24.bmp'
# image_size = im_gray.shape


# def plot_one_box(img, color=None, label=None, line_thickness=None):
#     ## Reading an image in default mode
#     image = cv2.imread(img)
#
#     ## Start coordinate, here (5, 5)
#     ## represents the top left corner of rectangle
#     start_point = (0, 0)
#
#     ## Ending coordinate, here (220, 220)
#     ## Represents the bottom right corner of rectangle
#     end_point = im_gray
#
#     ## Blue color in BGR
#     color = (255, 0, 0)
#
#     ## Line thickness of 2 px
#     thickness = 2
#
#     ## Using cv2.rectangle() method
#     ## Draw a rectangle with blue line borders of thickness of 2 px
#     image = cv2.rectangle(image, start_point, end_point, color, thickness)

def plot_one_circle(img,x,y):
    ## Reading an image in default mode
    image = cv2.imread(img)

    ## Dimensions of image
    img_shape = image.shape


    ## Center coordinates
    center_coordinates = (int((x*.96)), (int((y*.96))))

    ## Radius of circle
    radius = 10   #30

    ## Red color in BGR
    color = (0, 0, 255)

    ## Line thickness of -1 px
    thickness = -1

    ## Using cv2.circle() method
    ## Draw a circle of red color of thickness -1 px
    image = cv2.circle(image, center_coordinates, radius, color, thickness)

    return image


def get_paths():

    paths = []
    for path in FILE_PATHS:
        paths.append(openfiledialog(path))

    return paths


def plot_coords(centroid, image,starting_dir, columns):
    ## Used to stop Pandas from truncating long strings
    pd.options.display.max_colwidth = 2000

    img = cv2.imread(image)
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image_size = im_gray.shape


    df = pd.read_excel(centroid,header=None)
    df.columns = columns

    tup_one = image_size[0]
    tup_two = image_size[1]
    grid_size = (tup_two, tup_one)

    coordinates = np.empty(grid_size)

    for i, row in df.iterrows():

        Ref_Part_Num = row[columns[0]]
        Part_Num = row[columns[1]]

        x = int(row[columns[2]])
        y = int((image_size[0] * 1.04) - row[columns[3]])

        coordinates[x,y] = 1

        print(Ref_Part_Num)

        save_path = os.path.join(starting_dir, "temporary.tif")

        plot = plot_one_circle(image,x,y)
        cv2.imwrite(save_path,plot)

        image = r'C:\Users\rburns\Desktop\ZFirst\temporary.tif'
        #break

    print(coordinates)
    # ## convert your array into a dataframe
    # df = pd.DataFrame (coordinates)
    #
    # ## save to xlsx file
    #
    # filepath = r'C:\Users\rburns\Documents\Dataframe Out\my_excel_file.xlsx'
    #
    # df.to_excel(filepath, index=False)



if __name__ == "__main__":

    Data_Path = get_paths()

    plot_coords(centroid=Data_Path[0], image=Data_Path[1], starting_dir=FILE_PATHS[1], columns=HEADER)
