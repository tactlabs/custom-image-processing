'''
Created on Nov 22, 2022
Course work: 
@author: Vijitha, Joy, Krithiga
Source:
    
'''


from wand.image import Image
from os import listdir
from os.path import isfile, join
import cv2
import pytesseract

#oreo = Image(filename ='SL1500.jpg')
##print(oreo.height, oreo.width)



def get_files():
    oreo = [f for f in listdir('Images/Oreo') if isfile(join('Images/Oreo', f))]
    print(oreo)
    

def image_resize():
    for img in get_files.oreo:
        resize_oreo=oreo.resize(1000,1000)
        return oreo.width,oreo.height

if __name__== "__main__":
    #resize_width,resize_height=image_resize()
    #print(resize_width,resize_height)
    get_files()