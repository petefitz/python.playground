import cv2
import numpy as np
from datetime import datetime
from collections import deque

trim_data=deque([],maxlen=100) #store the last 100 readings- deque means "double ended queue"
margin=float(30) #percentage above background that the camera must detect
cam = cv2.VideoCapture(0)

def diffImg(t0, t1, t2): #work out the differences between the three images
	d1 = cv2.absdiff(t2, t1) #compare the second and third
	d2 = cv2.absdiff(t1, t0) #compare the first and second
	return cv2.bitwise_and(d1, d2) #an array containing 1s where there's a difference

def trim(difference): #work out a rolling threshold based on current viewing conditions
	trim_data.append(difference) #add the most recent difference to the set of up to 100 - if 100 are already recorded, the deque automatically removes the oldest
	average=np.mean(trim_data)#calculate an average of those differences
	threshold=average+int(average*(margin/100)) #recalculate current threshold based on viewing conditions
	return threshold

def preview(stream):
	winName = "Motion Detection"
	cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
	cv2.imshow( winName, stream )
	
def grab():	#grab a frame
	frame=cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY) #grab frame, convert to grey
	frame=cv2.medianBlur(frame,13) #blur it to reduce noise
	frame=cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,3) #apply threshold to convert pixels above a certain value to black, all others to white
	return frame

#BEGIN CODE	
# Read three images first to get the party started:
frame_minus=grab()
frame=grab()
frame_plus=grab()

while True:
	motion=False
	file_name=""
	
	# Read next image
	frame_minus = frame
	frame = frame_plus
	frame_plus = grab()
	
	preview(frame_plus) #show a preview of the current image - turn off when in use
	dimg=diffImg(frame_minus, frame, frame_plus) # create an array of the changed pixels
	difference=cv2.countNonZero(dimg) #how many 1s are there in dimg = difference level
	threshold=trim(difference) #what is the threshold in current viewing conditions?
	print difference # for monitoring purposes
	
	if difference > threshold: #is the difference enough to trigger a shot?
		file_name='c:/temp/images/'+datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss_%f') + '.jpg'
		cv2.imwrite(file_name, cam.read()[1],[int(cv2.IMWRITE_JPEG_QUALITY), 60])#write the file at 60% compression
		motion=True 
  
	key = cv2.waitKey(200) #pause for 200 milliseconds 
	if motion==True:
		pass
		#upload to dropbox here
	
	if key == 27: #if the user presses esc
		break

