import cv2
import numpy as np

import paths
from Server import SocketServer
import constants


def mask_preproscessing(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    kernel_5 = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))

    _, threshold = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)

    closing = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)
    closing = cv2.morphologyEx(closing, cv2.MORPH_CLOSE, kernel)
    closing = cv2.morphologyEx(closing, cv2.MORPH_CLOSE, kernel)
    closing = cv2.morphologyEx(closing, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
    blur = cv2.GaussianBlur(opening, (5, 5), 0)

    # cv2.imshow("after blur", blur)
    closing = cv2.morphologyEx(blur, cv2.MORPH_CLOSE, kernel)

    # cv2.imshow("after closing", closing)
    threshold = cv2.dilate(closing, kernel_5)
    threshold = cv2.dilate(threshold, kernel_5)
    threshold = cv2.dilate(threshold, kernel_5)
    threshold = cv2.dilate(threshold, kernel_5)
    threshold = cv2.erode(threshold, kernel_5)

    cv2.imshow("after dilation", threshold)
    return threshold


def start():
    serverData = SocketServer()

    EW_videoCapture = cv2.VideoCapture(paths.EW_VIDEO_PATH)
    NS_videoCapture = cv2.VideoCapture(paths.NS_VIDEO_PATH)

    bgSubtractor = cv2.createBackgroundSubtractorMOG2(varThreshold=230, detectShadows=True)

    # frameWidth = int(videoCapture.get(3))
    # frameHeight = int(videoCapture.get(4))
    # linePoint1 = (0, int(frameHeight / 2))
    # linePoint2 = (frameWidth, int(frameHeight / 2))

    while True:

        _, EW_frame = EW_videoCapture.read()
        _, NS_frame = EW_videoCapture.read()

        # cv2.line(frame, linePoint1, linePoint2, (0, 0, 255), 2)

        EW_fgMask = bgSubtractor.apply(EW_frame)
        NS_fgMask = bgSubtractor.apply(NS_frame)

        EW_fgMask = mask_preproscessing(EW_fgMask)
        NS_fgMask = mask_preproscessing(NS_fgMask)

        EW_contours, _ = cv2.findContours(EW_fgMask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        NS_contours, _ = cv2.findContours(NS_fgMask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        serverDataStr = str(len(NS_contours)) + "+" + str(len(EW_contours))
        print(serverDataStr)
        serverData.send(serverDataStr)

        cv2.drawContours(EW_frame, EW_contours, -1, (0, 255, 0), 2)
        cv2.drawContours(NS_frame, NS_contours, -1, (0, 255, 0), 2)

        cv2.imshow("EW_Contours", EW_frame)
        cv2.imshow("NS_Contours", NS_frame)

        key = cv2.waitKey(50)
        if key == 27:
            break

    EW_videoCapture.release()
    NS_videoCapture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start()
