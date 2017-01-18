#!/bin/python

from __future__ import division
from time import sleep
import Adafruit_PCA9685
#from picamera import PiCamera
import os
#import time
#from neopixel import *
import pprint

print '#######################'
print '# PiBot OS  :::  v0.8 #'
print '#######################'
print ''
print '[INFO][STARTUP] Modules Loaded:'
print ' \------------> "division" from "__future__"'
print ' \------------> "sleep" from "time"'
print ' \------------> "Adafruit_PCA9685"'
print ' \------------> "os"'

#camera = PiCamera()
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

print '[INFO][STARTUP] Initialized PWM HAT.'

#Infared Vision
file = open('/sys/class/gpio/export', 'w')
sleep(0.1)
file.write('13')
sleep(0.1)
try:
    file.close()
except:
    pass
sleep(0.1)
file = open('/sys/class/gpio/gpio13/direction', 'w')
sleep(0.1)
file.write('out')
sleep(0.1)
file.close()
sleep(0.1)
irvf = '/sys/class/gpio/gpio13/value'

print '[INFO][STARTUP] Initialized IR LED(s).'

# LED strip configuration:
LED_COUNT   = 1      # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

# Create NeoPixel object with appropriate configuration.
#strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
# Intialize the library (must be called once before other functions).
#strip.begin()
#print '[INFO][STARTUP] Initialized NeoPixel LED(s).'

def drive(time, rspeed, lspeed):
    #time in seconds; speed in pwm
    right = 533 - rspeed
    rpwm = int(right)
    left = 433 + lspeed
    lpwm = int(left)
    pwm.set_pwm(0, 0, rpwm)
    pwm.set_pwm(1, 0, lpwm)
    sleep(time)
    pwm.set_pwm(0, 0, 483)
    pwm.set_pwm(1, 0, 483)
    return;

def home():
    pwm.set_pwm(2, 0, 315)
    pwm.set_pwm(3, 0, 350)

def gimbal(x, y):
    pwm.set_pwm(2, 0, x)
    pwm.set_pwm(3, 0, y)

def preset(p):
    if p == 0:
        home()
    elif p == 1:
        gimbal(330, 400)
    elif p ==2:
        gimbal(330, 300)
    elif p == 3:
        gimbal(330, 200)
    elif p == 4:
        gimbal(250, 350)
    elif p == 5:
        gimbal(250, 400)
    elif p == 6:
        gimbal(250, 300)
    elif p == 7:
        gimbal(250, 200)
    elif p == 8:
        gimbal(130, 350)
    elif p == 9:
        gimbal(130, 400)
    elif p == 10:
        gimbal(130, 300)
    elif p == 11:
        gimbal(130, 200)
    elif p == 12:
        gimbal(410, 350)
    elif p == 13:
        gimbal(410, 400)
    elif p == 14:
        gimbal(410, 300)
    elif p == 15:
        gimbal(410, 200)
    elif p == 16:
        gimbal(560, 350)
    elif p == 17:
        gimbal(560, 400)
    elif p == 18:
        gimbal(560, 300)
    elif p == 19:
        gimbal(560, 200)
    elif p == 20:
        preset(8)
        i = 0
        d = 0
        while True:
            if d == 0:
                if i > 560:
                    d = 5
                gimbal(i + 130, 350)
                i = i + 5
            else:
                if i < 130:
                    d = 5
                gimbal(i + 130, 350)
                i = i - 5
            sleep(0.125)

def stop():
    drive(0, 50,50)

def arm(x, y, z, g):
    #pwm.set_pwm(15, 0, x)
    pwm.set_pwm(7, 0, y)
    #pwm.set_pwm(15, 0, z)
    pwm.set_pwm(6, 0, g)

def armHome():
    arm(450, 200, 0, 0)

gres = 25
gimbalx = 330
gimbaly = 350
home()

ares = 25
armx = 450
army = 200
armz = 0
armg = 0
armHome()

ir = 0
movtog = 0

print '[INFO][STARTUP] finalizing...'
print '[INFO][STARTUP] DONE!'

while True:
    fexist = os.path.isfile('/var/www/downlink')
    if fexist == True:
        file = open("/var/www/downlink", "r")
        cmd = file.read()
	print '[INFO] Command recieved:  " %s "' % cmd
        if cmd == "mov-stop":
            stop()
        elif cmd == "mov-up":
            if movtog == 1:
                pwm.set_pwm(0, 0, 483)
                pwm.set_pwm(1, 0, 483)
                movtog = 0
            else:
                drive(1, 100, 100)
        elif cmd == "toggle-mov-up":
            if movtog == 0:
                right = 533 - 100
                rpwm = int(right)
                left = 433 + 100
                lpwm = int(left)
                pwm.set_pwm(0, 0, rpwm)
                pwm.set_pwm(1, 0, lpwm)
                movtog = 1
            elif movtog == 1:
                pwm.set_pwm(0, 0, 483)
                pwm.set_pwm(1, 0, 483)
                movtog = 0
        elif cmd == "mov-left":
            drive(0.5, 75, 25)
        elif cmd == "mov-right":
            drive(0.5, 25, 75)
        elif cmd == "mov-down":
            drive(1, 25, 25)
        elif cmd == "mov-fleft":
            drive(1, 55, 45)
        elif cmd == "mov-fright":
            drive(1, 45, 55)
        elif cmd == "mov-fup":
            drive(1, 60, 60)
        elif cmd == "mov-fdown":
            drive(1, 55, 55)
        elif cmd == "gim-left":
            x = gimbalx
            gimbalx = x + 25
            gimbal(gimbalx, gimbaly)
        elif cmd == "gim-right":
            x = gimbalx
            gimbalx= x - 25
            gimbal(gimbalx, gimbaly)
        elif cmd == "gim-down":
            y = gimbaly
            gimbaly = y + 25
            gimbal(gimbalx, gimbaly)
        elif cmd == "gim-up":
            y = gimbaly
            gimbaly = y - 25
            gimbal(gimbalx, gimbaly)
        elif cmd == "gim-home":
            home()
            gimbalx = 330
            gimbaly = 350
        elif cmd == "man-right":
            x = armx
            armx = x + ares
            arm(armx, army, armz, armg)
        elif cmd == "man-left":
            x = armx
            armx = x - ares
            arm(armx, army, armz, armg)
        elif cmd == "man-down":
            y = army
            army = y + ares
            arm(armx, army, armz, armg)
        elif cmd == "man-up":
            y = army
            army = y - ares
            arm(armx, army, armz, armg)
        elif cmd == "manout":
            z = armz
            armz = z + ares
            arm(armx, army, armz, armg)
        elif cmd == "man-in":
            z = armz
            armz = z - ares
            arm(armx, army, armz, armg)
        elif cmd == "man-close":
            pwm.set_pwm(6, 0, 200)
        elif cmd == "man-open":
            pwm.set_pwm(6, 0, 400)
        elif cmd == "man-home":
            armHome()
        elif cmd == "ir-toggle":
            if ir == 0:
                irf = open(irvf, 'w')
                irf.write('1')
                irf.close()
                ir = 1
            elif ir == 1:
                irf = open(irvf, 'w')
                irf.write('0')
                irf.close()
                ir = 0
        else:
            print '[ERROR] Command not found!'
    	try:
            os.remove("/var/www/downlink")
        except OSError:
            print '[INFO][ERROR][HANDLED] Tried to remove an inexistant file.'