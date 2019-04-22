import cv2
import numpy as np

import paths
import constants


def mask_preproscessing(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

    # Fill any small holes
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    # Remove noise
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

    blur = cv2.blur(opening, (2, 2))

    # Dilate to merge adjacent blobs
    dilation = cv2.dilate(blur, kernel, iterations=40)

    _, th = cv2.threshold(dilation, 240, 255, cv2.THRESH_BINARY)

    return th


def start():
    videoCapture = cv2.VideoCapture(paths.VIDEO_PATH)
    bgSubtractor = cv2.createBackgroundSubtractorMOG2(varThreshold=210, detectShadows=True)

    while True:

        _, frame = videoCapture.read()

        fgMask = bgSubtractor.apply(frame)
        fgMask = mask_preproscessing(fgMask)

        contours, _ = cv2.findContours(fgMask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        print(len(contours))

        cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

        cv2.imshow("fgMask", frame)

        key = cv2.waitKey(33)
        if key == 27:
            break

    videoCapture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start()
