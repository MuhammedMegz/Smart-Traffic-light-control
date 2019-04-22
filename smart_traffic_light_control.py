# # imports
#
# import os
# import random
#
# import skvideo.io
#
# import logging
# import logging.handlers
#
# import cv2
#
# import paths
# import constants
#
# cv2.ocl.setUseOpenCL(False)
# random.seed(123)
#
#
# def background_subtractor_taining(bgSubtractor, videoCapture):
#     """
#       apply some frames to detect the most reliable background
#     """
#
#     logging.info('start training the background subtrator')
#
#     i = 0
#
#     for eachFrame in videoCapture:
#         bgSubtractor.apply(eachFrame, None, constants.LEARNING_RATE)
#         i += 1
#         if i >= constants.TRAINING_FRAMES_NO:
#             return videoCapture
#
#
# def start():
#     # use Mixture of Gaussian algorithm built in openCV to create background subtractor
#     bgSubtractor = cv2.createBackgroundSubtractorMOG2(constants.TRAINING_FRAMES_NO, varThreshold=25, detectShadows=True)
#
#     videoCapture = skvideo.io.vreader(paths.VIDEO_PATH)
#
#     # apply the background subtractor to the train function to extract the background from the loaded video
#     videoCapture = background_subtractor_taining(bgSubtractor, videoCapture)
#
#     frame_number = -1
#
#     for frame in videoCapture:
#         if not frame.any():
#             logging.error("Frame capture failed, stopping...")
#             break
#
#         frame_number += 1
#
#         cv2.imwrite("/Volumes/SSD 1/Smart-Traffic-light-control1/output/" + str(frame_number) + ".png", frame)
#
#         fgmask = cv2.BackgroundSubtractor.apply(frame, fgmask , constants.LEARNING_RATE)
#
#         cv2.imwrite("/Volumes/SSD 1/Smart-Traffic-light-control1/output/for_" + str(frame_number) + ".png", frame)
#
#
# if __name__ == "__main__":
#
#     if not os.path.exists(paths.IMAGE_PATH):
#         os.makedirs(paths.IMAGE_PATH)
#
#     start()
