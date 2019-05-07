import cv2
import numpy as np

import paths
from Server import SocketServer
import constants
import time, threading

serverData = SocketServer()
serverDataStr = ""

def send_periodicly():
    if serverDataStr != "":
    	serverData.send(serverDataStr)
    	print("send: " + serverDataStr)
    threading.Timer(10, send_periodicly).start()


def mask_preproscessing(img):


    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))

    # Fill any small holes
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)
    # Remove noise
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel, iterations=1)

    # Dilate to merge adjacent blobs
    dilation = cv2.dilate(opening, kernel, iterations=2)

    # threshold
    _ , th = cv2.threshold(dilation, 240, 255, cv2.THRESH_BINARY)
    
    final = th
    #cv2.imshow("after dilation", final)
    return final   


def start():

    EW_videoCapture = cv2.VideoCapture(paths.EW_VIDEO_PATH)
    NS_videoCapture = cv2.VideoCapture(paths.NS_VIDEO_PATH)

    EW_bgSubtractor = cv2.createBackgroundSubtractorMOG2(history=500, detectShadows=False)
    NS_bgSubtractor = cv2.createBackgroundSubtractorMOG2(history=500, detectShadows=False)

    # frameWidth = int(videoCapture.get(3))
    # frameHeight = int(videoCapture.get(4))
    # linePoint1 = (0, int(frameHeight / 2))
    # linePoint2 = (frameWidth, int(frameHeight / 2))

    while True:

        _, EW_frame = EW_videoCapture.read()
        _, NS_frame = NS_videoCapture.read()

        EW_fgMask = EW_bgSubtractor.apply(EW_frame)
        NS_fgMask = NS_bgSubtractor.apply(NS_frame)

        EW_fgMask = mask_preproscessing(EW_fgMask)
        NS_fgMask = mask_preproscessing(NS_fgMask)

        EW_contours, _ = cv2.findContours(EW_fgMask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        NS_contours, _ = cv2.findContours(NS_fgMask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        EWCount = 0
        NSCount = 0

        # filtering by with, height
        for (i, contour) in enumerate(EW_contours):

            (x, y, w, h) = cv2.boundingRect(contour)
            contour_valid = (w >= 40) and (
            h >= 40)

            if not contour_valid:
                continue
            
            cv2.rectangle(EW_frame, (x, y), (x+w, y+h), (0,255,0),3)
            EWCount+=1

        # filtering by with, height
        for (i, contour) in enumerate(NS_contours):

            (x, y, w, h) = cv2.boundingRect(contour)
            contour_valid = (w >= 40) and (
            h >= 40)

            if not contour_valid:
                continue
            
            cv2.rectangle(NS_frame, (x, y), (x+w, y+h), (0,255,0),3)
            NSCount+=1
	    

	
        global serverDataStr
        serverDataStr = str(NSCount) + "," + str(EWCount)
        #print("NS: " + str(NSCount) + ", EW: " + str(EWCount))


        cv2.imshow("EW_Contours", EW_frame)
        cv2.imshow("NS_Contours", NS_frame)

        key = cv2.waitKey(25)
        if key == 27:
            break

    EW_videoCapture.release()
    NS_videoCapture.release()
    cv2.destroyAllWindows()
    serverData.close()


if __name__ == "__main__":
    send_periodicly()
    start()
    
