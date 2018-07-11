
# coding: utf-8

# In[ ]:

from PIL import ImageGrab
import time
currenttime=datetime.datetime.now()
endtime=currenttime + datetime.timedelta(hours = 1)
directory="C:\\Users\\ysaxe2\\Desktop\\shots\\"
name="screen_capture"
start=1
while endtime>currenttime:
    time.sleep(1)
    filename=directory+name+str(start)+".jpg"
    ImageGrab.grab().save(filename, "JPEG")
    start=start+1
    currenttime=datetime.datetime.now()
    print "Running......","Pic ",start,"taken."     

