from PIL import Image
from tkinter import filedialog
import PIL
import os
import glob
import time
import concurrent.futures


class ConvertImage():
    def __init__(self , PathInputFolder , PathOutputFolder , ForamtOutput , FAST=True) -> None:
        self.FAST = FAST
        self.PathInput = PathInputFolder
        self.PathOutput = PathOutputFolder
        self.FormatsInput  = ('jpg' , 'png' , 'webp')
        self.FormatsOutput = ('jpg' , 'png' , 'webp')
        self.FormatOutout = ForamtOutput
    
    def FindImages(self):
        # Get the files and folders in the input folder
        ListDir = os.listdir(self.PathInput)
        
        Images = list()
        # Filter photos
        for item in ListDir :
            item = item.split('.')
            if item[-1] in self.FormatsInput:
                name = ''
                for l in item[:-1]: name += '.' + l
                name = name[1:]
                Images.append((name,item[-1]))
        
        self.Images = Images
    def ConvertImage(self , Photo):
        pass
    
    def Run(self):
        pass


