'''
Created on Nov 22, 2022
Course work: 
@author: Vijitha, Joy, Krithiga
Source:
    
'''


from wand.image import Image

oreo = Image(filename ='SL1500.jpg')
##print(oreo.height, oreo.width)

def image_resize():
    resize_oreo=oreo.resize(1000,1000)
    return oreo.width,oreo.height


if __name__== "__main__":
    resize_width,resize_height=image_resize()
    print(resize_width,resize_height)