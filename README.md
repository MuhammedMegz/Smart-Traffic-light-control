# Smart-Traffic-light-control

##  Introduction 

This project was made to manage traffic time dynamicly between two directions in main square by splitting time fairly between the two directions depending on the direction with high flow of cars and vehicles.

The side with the high flow have larger time to grant it's vehicles to pass untill the case change or finished it's time.

We adopted to work purely image processing and not using any kind of AI or Machine Learning stuff and make it so simple,
We used openCV functions and features not adding any third party stuff.

## Table of contents:

* [Car Detection](#Car-Detection)
* [Time Divison](#Time-division)
* [GUI](#GUI)

## Car Detection:
  
  We used Background subtraction tools to detect the background and trained out application for the first 500 frame, to detect the best and the most reliable background.
  
```
$ EW_bgSubtractor = cv2.createBackgroundSubtractorMOG2(history=500, detectShadows=False)
$ NS_bgSubtractor = cv2.createBackgroundSubtractorMOG2(history=500, detectShadows=False)
```
  
  Then we make some processing for image quality like openning, closing, dilation, erosion, and blur to draw our contours perfectly, after that thresholding the detected contours to extract the best ones and to be counted as the number of moving vehicles.
  
 ![alt text](https://cdn-images-1.medium.com/max/800/0*iNYtQubKAtK0OGG5.png)
  
Finally, Drawing the boxes for detected cars to make sure that the output is correct after this long term processes.
  
```
$ EW_bgSubtractor = cv2.createBackgroundSubtractorMOG2(history=500, detectShadows=False)
$ NS_bgSubtractor = cv2.createBackgroundSubtractorMOG2(history=500, detectShadows=False)
```
  
## Time Divison:

  Time division was the smartest and the main part here to write logic to manage all the scenarios
  
  ```
  $ if waited_time < min_waited_time :
        waited_time = min_waited_time
  $ elif waited_time > max_waited_time :
        waited_time = max_waited_time
  ```
  
## GUI: 

  Using Python Tkinter library to build the GUI, first we made a animation to simulate which direction is granted to move, 
  add to this the traffic lights it self animated also.
  
  Then communicating to the time division part and car detection part using socket.io library, it was best choice to not getting any code injection.
