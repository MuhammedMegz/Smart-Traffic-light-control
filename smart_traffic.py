import cv2
import numpy as np

import paths
import constants


def mask_preproscessing(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    kernel_5 = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))

    _, threshold = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)

    opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
    blur = cv2.GaussianBlur(opening, (5, 5), 0)
    # cv2.imshow("after blur", blur)
    closing = cv2.morphologyEx(blur, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow("after closing", closing)
    threshold = cv2.dilate(closing, kernel_5)
    threshold = cv2.dilate(threshold, kernel_5)
    threshold = cv2.erode(threshold, kernel_5)

    threshold = cv2.dilate(threshold, kernel_5)
    threshold = cv2.dilate(threshold, kernel_5)
    threshold = cv2.erode(threshold, kernel_5)
    cv2.imshow("after dilation", threshold)
    return threshold


def start():
    videoCapture = cv2.VideoCapture(paths.VIDEO_PATH)
    bgSubtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=230, detectShadows=True)

    frameWidth = int(videoCapture.get(3))
    frameHeight = int(videoCapture.get(4))
    linePoint1 = (0, int(frameHeight / 2))
    linePoint2 = (frameWidth, int(frameHeight / 2))

    while True:

        _, frame = videoCapture.read()

        cv2.line(frame, linePoint1, linePoint2, (0, 0, 255), 2)

        fgMask = bgSubtractor.apply(frame)

        fgMask = mask_preproscessing(fgMask)

        contours, _ = cv2.findContours(fgMask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        print(len(contours))

        cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

        cv2.imshow("fgMask", frame)

        key = cv2.waitKey(50)
        if key == 27:
            break

    videoCapture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start()
