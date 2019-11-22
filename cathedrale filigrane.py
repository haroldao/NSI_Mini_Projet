from __future__ import print_function
import numpy as np
import cv2
 
image = cv2.imread("./hanif.jpg")
 
def addWaterMark(text,opacity,BGRColor):
    opacity=opacity/100
    overlay = image.copy()
    output = image.copy()
 
    cv2.putText(overlay, text, (0,int(2*(image.shape[1])/3)), cv2.FONT_HERSHEY_SIMPLEX, 1.0, BGRColor, 2)
    cv2.addWeighted(overlay, opacity, output, 1 - opacity,
                    0, output)
    cv2.imshow("Output", output)
    cv2.waitKey(0)
 
if __name__ == '__main__':
    addWaterMark("Life2Coding",50,(255,0,255))

