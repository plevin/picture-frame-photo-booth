# modules that you want to import
import time
import sys
from time import sleep
from picamera import PiCamera
from os import system
import os
from gpiozero import Button
import shutil
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

button = Button(3)
camera = PiCamera()
camera.resolution = (1024, 768)
camera.vflip = False

# initialize pygame

screen_width=1920
screen_height=1080
pygame.init()
pygame.display.set_mode([screen_width,screen_height])
screen = pygame.display.get_surface()
pygame.display.set_caption('Photo Booth Pics')
pygame.mouse.set_visible(False) #hide the mouse cursor
pygame.display.toggle_fullscreen()

now = time.strftime("%Y-%m-%d-%H-%M-%S") #get the current date and time for the start of the filename

button.wait_for_press()

def take_photos():
    input(pygame.event.get())
    
    try:
        camera.start_preview()
        sleep(2)
        for i in range (0,6):
            filename = now + '-0' + str(i) + '.jpg'
            camera.stop_preview()
            camera.capture("makegif/" + filename)
            camera.start_preview()
            time.sleep(.5)
    finally:
        camera.close()
        graphicsmagick = 'gm convert -delay 20 ~/PiBooth/makegif/*.jpg ~/PiBooth/test.gif'
        os.system(graphicsmagick)
        cleanup = 'rm /home/pi/PiBooth/makegif/*.jpg' # cleanup source images
        os.system(cleanup)
        os.rename('/home/pi/PiBooth/test.gif', '/home/pi/PiBooth/archive/' + now + '.gif')
    # End of the function
    
take_photos()


# try:
#    camera.start_preview()
#    sleep(2)
#    for i in range (0,6):    
#        filename = now + '-0' + str(i) + '.jpg'
#        camera.stop_preview()
#        camera.capture("makegif/" + filename)
#        camera.start_preview()
#        time.sleep(.5)
#finally:
#    camera.close()
#    graphicsmagick = 'gm convert -delay 20 ~/PiBooth/makegif/*.jpg ~/PiBooth/test.gif'
#    os.system(graphicsmagick)
#    cleanup = 'rm /home/pi/PiBooth/makegif/*.jpg' # cleanup source images
#    os.system(cleanup)
#    os.rename('/home/pi/PiBooth/test.gif', '/home/pi/PiBooth/archive/' + now + '.gif')

