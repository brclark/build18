#!/usr/bin/env python
import cv
import freenect
import frame_convert

def get_video():
	return frame_convert.video_cv(freenect.sync_get_video()[0])

def detect(image):
	image_size = cv.GetSize(image)

	#create greyscale version
	grayscale = cv.CreateImage(image_size, 8, 1)
	cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)

	# create storage
	storage = cv.CreateMemStorage(0)
	#cv.ClearMemStorage(storage)

	# equalize histogram
	cv.EqualizeHist(grayscale, grayscale)

	# detect objects
	cascade = cv.Load('haarcascade_frontalface_alt.xml')
	faces = cv.HaarDetectObjects(grayscale, cascade, storage, 1.2, 2, cv.HAAR_DO_CANNY_PRUNING, CV.SIZE(50,50))

	if faces:
		print 'face detected!'
		for i in faces:
			cv.Rectangle(image, cv.Point( int(i.x), int(i.y)),
								cv.Point(int(i.x + i.width), int(i.y + i.height)),
								cv.RGB(0,255,0), 3, 8, 0)
	
	cv.ShowImage('Video', image)

	return faces

while(1):
	detect(get_video())
