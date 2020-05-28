import pyautogui
from PIL import Image , ImageGrab
import time
#from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)

#def draw():
    #for i in range(34,45):
       #for j in range(45,67):

def isCollide(data):
    for i in range(300,315):
            for j in range(425,480):
                if data[i,j]  < 100:
                    return True
    return False



if __name__ == "__main__":
    print("Dino is going to run in 3 sec")
    time.sleep(3)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            hit("up")
        #print(asarray(image))
        
    #image.show()