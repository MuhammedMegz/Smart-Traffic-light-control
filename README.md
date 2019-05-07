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
* [How to use (Ubuntu/Linux)](#How-to-use-(Ubuntu/Linux))
## Car Detection:
  
  We used Background subtraction tools to detect the background and trained out application for the first 500 frame, to detect the best and the most reliable background.
  
```
$ EW_bgSubtractor = cv2.createBackgroundSubtractorMOG2(history=500, detectShadows=False)
$ NS_bgSubtractor = cv2.createBackgroundSubtractorMOG2(history=500, detectShadows=False)
```
  
   ![alt text](https://cdn-images-1.medium.com/max/800/0*iNYtQubKAtK0OGG5.png)
   
   
  Then we make some processing for image quality like openning, closing, dilation, erosion, and blur to draw our contours perfectly, after that thresholding the detected contours to extract the best ones and to be counted as the number of moving vehicles.
  
```
 closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)
 opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel, iterations=1)
 dilation = cv2.dilate(opening, kernel, iterations=2)
 _ , th = cv2.threshold(dilation, 240, 255, cv2.THRESH_BINARY)
```
  
Finally, Drawing the boxes for detected cars to make sure that the output is correct after this long term processes.
  
```
 EW_contours, _ = cv2.findContours(EW_fgMask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
 NS_contours, _ = cv2.findContours(NS_fgMask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
```
```
 for (i, contour) in enumerate(EW_contours):
    (x, y, w, h) = cv2.boundingRect(contour)
     contour_valid = (w >= 40) and (
            h >= 40)

           if not contour_valid:
                continue
           
           cv2.rectangle(EW_frame, (x, y), (x+w, y+h), (0,255,0),3)
           EWCount+=1
```
 
 
## Time Divison:

  Time division was the smartest and the main part here to write logic to manage all the scenarios
  
  ```
    if turn=="EW":
        # the turn is on EW
        if right_traffic_num >= forward_traffic_num:
            return "no change"
        return waited_time(right_traffic_num,forward_traffic_num)

      
    if turn=="NS":
        # the turn is on NS
        if forward_traffic_num >= right_traffic_num:
            return "no change"
        return waited_time(forward_traffic_num,right_traffic_num)
  ```
  
## GUI: 

  Using Python Tkinter library to build the GUI, first we made a animation to simulate which direction is granted to move, 
  add to this the traffic lights it self animated also.
  
  Then communicating to the time division part and car detection part using socket.io library, it was best choice to not getting any code injection.
  
## How to use (Ubuntu/Linux):
   - Download all files in the repo, the files might exceed 50MB because of the video which the model work on.
   - Un-zip
   - Open the un-zipped file then open a new terminal inside this file directory.
   - Execute "run.sh" script using this line "./run.sh" in terminal to run the program, you may need to change permissions for this          script using this line "chmod u+x run.sh".
   - This script will run 2 new terminals and 3 windows, one for the traffic light simulation, one for the North-South road with the          detected contours and one for the East-West road with detected contours.
