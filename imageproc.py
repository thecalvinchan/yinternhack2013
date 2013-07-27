#!/usr/bin/python

import cv
import argparse
import json

##Settings

MIN_SIZE = (20, 20)
IMAGE_SCALE = 2
HAAR_SCALE = 1.2
MIN_NEIGHBORS = 2
HAAR_FLAGS = 0
HAAR_TRAINER = "haarcascade_frontalface_alt.xml"

def procImag(images,data):
  cascade = cv.Load(HAAR_TRAINER)
  for image_name in images:
    #Allocate Space for grayscale image and tiny image
    #Dramatically reduces computation time in exchange for temporary space
    image = cv.LoadImage(image_name, 1)
    grayscale = cv.CreateImage((image.width,image.height),8,1)
    img = cv.CreateImage((cv.Round(image.width/IMAGE_SCALE),cv.Round(image.height/IMAGE_SCALE)),8,1)
    cv.CvtColor(image,grayscale,cv.CV_BGR2GRAY)
    cv.Resize(grayscale,img,cv.CV_INTER_LINEAR)
    cv.EqualizeHist(img,img)
    matches = cv.HaarDetectObjects(img,cascade,cv.CreateMemStorage(0),HAAR_SCALE,IMAGE_SCALE,HAAR_FLAGS,MIN_SIZE)
    temp = []
    for ((x,y,width,height),wat) in matches:
      temp.append({"x":x,"y":y,"width":width,"height":height})
      #pt1 = (int(match[0][0] * IMAGE_SCALE), int(match[0][1] * IMAGE_SCALE))
      #pt2 = (int((match[0][0] + match[0][2]) * IMAGE_SCALE), int((match[0][1] + match[0][3]) * IMAGE_SCALE))
      #cv.Rectangle(image, pt1, pt2, cv.RGB(255, 0, 0), 3, 8, 0)
    #cv.ShowImage("result", image)
    data[image_name]=temp

def main():
  parser = argparse.ArgumentParser(description="#WAT")
  parser.add_argument('files', nargs='*')
  args = parser.parse_args()
  data = {}
  procImag(args.files,data)
  print(json.dumps(data))

if __name__ == "__main__":
  main()
