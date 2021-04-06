import random
import cv2
import pyodbc
import pandas as pd
import re
import autoit ## pip install pyautoit
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# autoit.win_active('Pick Place for 74380B - Excel')
# autoit.win_move('Pick Place for 74380B - Excel',0,0)

HEADER = ["REF", "PART_NUM", "X", "Y","ROTATION","f"]
##IMAGE = r"C:\Users\rburns\Documents\ZoneFirst\Fresh Air 2.tif" ## _GTO.png was prev. source
IMAGE = r'C:\Users\rburns\Documents\ZoneFirst\Fresh Air 2.tif'
SAVE_PATH = r'C:\Users\rburns\Documents\ZoneFirst\Fresh Air 2.tif'  ##test.png ,the previous file


def openfiledialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir=r"S:\Centroids\Z\ZONEFIRST\FRESH-AIR-CYC REV -") ##S:\Centroids
    return file_path

def plot_one_box(img, color=None, label=None, line_thickness=None):
    ## Reading an image in default mode
    image = cv2.imread(img)

    ## Start coordinate, here (5, 5)
    ## represents the top left corner of rectangle
    start_point = (5, 5)

    ## Ending coordinate, here (220, 220)
    ## Represents the bottom right corner of rectangle
    end_point = (220, 220)

    ## Blue color in BGR
    color = (255, 0, 0)

    ## Line thickness of 2 px
    thickness = 2

    ## Using cv2.rectangle() method
    ## Draw a rectangle with blue line borders of thickness of 2 px
    image = cv2.rectangle(image, start_point, end_point, color, thickness)

def plot_one_circle(img,x,y):
    ## Reading an image in default mode
    image = cv2.imread(img)

    ## Dimensions of image
    img_shape = image.shape


    ## Center coordinates
    center_coordinates = (int(x*47.21), int(y*47.21))  ##x,y

    ## Radius of circle
    radius = 30

    ## Red color in BGR
    color = (0, 255, 0)

    ## Line thickness of -1 px
    thickness = -1

    ## Using cv2.circle() method
    ## Draw a circle of red color of thickness -1 px
    image = cv2.circle(image, center_coordinates, radius, color, thickness)

    return image


def get_centroid():
    Centroid_Path = openfiledialog()

    if Centroid_Path == None:
        print("Bom was not selected")
        exit()

    else:
        return Centroid_Path



def get_coords(centroid_path, columns):
    ## Used to stop Pandas from truncating long strings
    pd.options.display.max_colwidth = 2000

    df = pd.read_csv(centroid_path,sep='\t',header=None)
    df.columns = columns

    for i, row in df.iterrows():

        Ref_Part_Num = row[columns[0]]
        Part_Num = row[columns[1]]
        y = row[columns[2]]
        x = row[columns[3]]

        print(Ref_Part_Num)

        plot = plot_one_circle(IMAGE,x,y)
        cv2.imwrite(SAVE_PATH,plot)
        ##break
        ## if i == 0:
        ##     break


if __name__ == "__main__":

    Centroid_Path = get_centroid()

    get_coords(Centroid_Path,HEADER)



