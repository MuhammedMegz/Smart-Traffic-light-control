# import cv2
# import paths
#
#
# def start():
#     videoCapture1 = cv2.VideoCapture(paths.VIDEO_PATH)
#     videoCapture2 = cv2.VideoCapture(paths.VIDEO_PATH)
#
#     frameWidth = int(videoCapture1.get(3))
#     frameHeight = int(videoCapture1.get(4))
#     linePoint1 = (0, int(frameHeight / 2))
#     linePoint2 = (frameWidth, int(frameHeight / 2))
#
#     while True:
#
#         _, frame1 = videoCapture1.read()
#         _, frame2 = videoCapture2.read()
#         cv2.line(frame1, linePoint1, linePoint2, (0, 0, 255), 2)
#
#         frame1_RGB = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
#         frame2_RGB = cv2.cvtColor(frame2, cv2.COLOR_RGB2GRAY)
#
#         frame1_RGB = cv2.GaussianBlur(frame1_RGB, (5, 5), 0)
#         frame1_RGB = cv2.GaussianBlur(frame2_RGB, (5, 5), 0)
#
#         abs_diff = cv2.absdiff(frame1_RGB, frame2_RGB, None)
#
#         _, threshold = cv2.threshold(abs_diff, 30, 255, cv2.THRESH_BINARY)
#
#         kernel_3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
#         kernel_5 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
#         kernel_7 = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
#         kernel_15 = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
#
#         threshold = cv2.dilate(threshold, kernel_5)
#         threshold = cv2.dilate(threshold, kernel_5)
#         threshold = cv2.erode(threshold, kernel_5)
#
#         threshold = cv2.dilate(threshold, kernel_5)
#         threshold = cv2.dilate(threshold, kernel_5)
#         threshold = cv2.erode(threshold, kernel_5)
#
#         cv2.imshow("frame1", threshold)
#
#         key = cv2.waitKey(33)
#         if key == 27:
#             break
#
#     videoCapture1.release()
#     cv2.destroyAllWindows()
#
#
# if __name__ == "__main__":
#     start()
