import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.patheffects as path_effects
import datetime
import matplotlib.dates as mdates
import csv
import matplotlib.image as mpimg
import matplotlib.cm as cm
import matplotlib.animation as animation
from matplotlib import style
import sys
import os

#-------------------------------------------------
himg = mpimg.imread("heart.jpg")
simg = mpimg.imread("sweat.gif")
pimg = mpimg.imread("paws.png")
bimg = mpimg.imread("body.png")
aimg = mpimg.imread("accelerometer.png")

#-------------------------------------------------
# heart value chart
#-------------------------------------------------
enumber = []
ename = []
edate = []
ex = []
ey = []
ez = []
gsr = []
gsrrange = []
hr = []
hrrange = []

#x = []
#y = []

fig = plt.figure()
heartchart = fig.add_subplot(3,3,3)
heartchart.grid(True)
heartchart.axis([0, 10, 60, 150])
style.use('ggplot')

def animate(i):
    graph_data = open('gsr.txt','r').read()
    lines = graph_data.split('\n')
    enumbers = []
    enames = []
    edates = []
    exs = []
    eys = []
    ezs = []
    gsrs = []
    gsrranges = []
    hrs = []
    hrranges = []
    
    #xs = []
    #ys = []
    
    for line in lines:
        if len(line) > 1:
            #x, y = line.split(',')
            enumber, ename, edate, ex, ey, ez, gsr, gsrrange, hrrange, hr = line.split(',')
            enumbers.append(enumber)
            enames.append(ename)
            edates.append(edate)
            exs.append(ex)
            eys.append(ey)
            ezs.append(ez)
            gsrs.append(gsr)
            gsrranges.append(gsrrange)
            hrs.append(hr)
            hrranges.append(hrrange)
            
            #xs.append(x)
            #ys.append(y)
    heartchart.clear()
    #heartchart.plot(xs, ys)
    heartchart.plot(enumbers, hrs)

ani = animation.FuncAnimation(fig, animate, interval=100)

#-------------------------------------------------
sweatchart = plt.subplot(3,3,6) #sweat value
sweatchart.axis([0, 10, 0, 10])
#dataset = pd.read_csv("example.csv")
#plt.title("Galvanic Skin Response")
#plt.plot(dataset.hart)


#-------------------------------------------------
# ACCELEROMETER VALUES
#plt.subplot(3,2,6) #accel value
plt.subplot(3,3,9)





#-------------------------------------------------
f = plt.subplot(3,3,2) #heart image
f.imshow(himg, cmap=cm.Greys_r)
f.set_title("Heart Rate")
f.axis('off')


#-------------------------------------------------
s = plt.subplot(3,3,5) #sweat image
s.imshow(simg, cmap=cm.Greys_r)
s.set_title("Sweating")
s.axis('off')

#-------------------------------------------------
b = plt.subplot(2,3,4) #person image
b.imshow(bimg, cmap=cm.Greys_r)
b.axis('off')



#-------------------------------------------------
t = plt.subplot(3,3,1) #wildcats title
t.set_title("Wildcats\n", fontsize=40, weight=800, va="center", ha="center")
t.imshow(pimg, cmap=cm.Greys_r)
t.axis('off')


#-------------------------------------------------
n = plt.subplot(6,3,7) #name
ndate = mdates.DateFormatter('%Y-%m-%d')
#n.set_title(ndate, fontsize=40, weight=700, va="top", ha="center")
#t.axis_border('on')


#-------------------------------------------------
#a = plt.subplot(3,6,15) #acclerometer image
a = plt.subplot(3,3,8) #acclerometer image
a.imshow(aimg, cmap=cm.Greys_r)
a.set_title("Acceleration")
a.axis('off')



#-------------------------------------------------
plt.show()
plt.axis('off')