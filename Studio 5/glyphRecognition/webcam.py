# Modified By: Callam Josef Jackson-Sem
# Project: Johnny 5 Robot
# Purpose Of File: Testing OpenCV's capabilities, in this case, the glyph recognition feature as well as shape tracking
# Description: This file is required in order for the files to gain access to and use the webcam. The file is also used to capture and update the
# frames to better render the given object within the frame window.

#imports need to use OpenCV commands and tools, as well as use the threading library module to better load the render webcam capture.
import cv2
from threading import Thread
  
class Webcam:
  
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        self.current_frame = self.video_capture.read()[1]
          
    # create thread for capturing images
    def start(self):
        Thread(target=self._update_frame, args=()).start()
  
    def _update_frame(self):
        while(True):
            self.current_frame = self.video_capture.read()[1]
                  
    # get the current frame
    def get_current_frame(self):
        return self.current_frame
