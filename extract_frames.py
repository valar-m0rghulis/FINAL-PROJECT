import pafy
import cv2
import math

url = "https://www.youtube.com/watch?v=Wjrrgrvq1ew"
videoPafy = pafy.new(url)
best = videoPafy.getbest()
video=cv2.VideoCapture(best.url)
frameRate = video.get(5) #frame rate
while(video.isOpened()):
    frameId = video.get(1) #current frame number
    ret, frame = video.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename = "C:/Users/chaud/Desktop/New folder (2)/image_" +  str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, frame)
video.release()
