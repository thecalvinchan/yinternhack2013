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
RENDER_IMAGES = False

def procImag(images,trainer):
  try:
    cascade = cv.Load(trainer)
  except TypeError:
    #print("Cascade file does not exist.")
    return 
  except:
    return
  else: 
    data = {}
    for image_name in images:
      try:
        image = cv.LoadImage(image_name, 1)
      except IOError:
        #print("No such file or directory")
        return 
      except:
        return
      else:
        #Allocate Space for grayscale image and tiny image
        #Dramatically reduces computation time in exchange for temporary space
        grayscale = cv.CreateImage((image.width,image.height),8,1)
        img = cv.CreateImage((cv.Round(image.width/IMAGE_SCALE),cv.Round(image.height/IMAGE_SCALE)),8,1)

        cv.CvtColor(image,grayscale,cv.CV_BGR2GRAY)
        cv.Resize(grayscale,img,cv.CV_INTER_LINEAR)
        cv.EqualizeHist(img,img)

        matches = cv.HaarDetectObjects(img,cascade,cv.CreateMemStorage(0),HAAR_SCALE,IMAGE_SCALE,HAAR_FLAGS,MIN_SIZE)
        temp = list()
        for ((x,y,width,height),wat) in matches:
          temp.append({"x":x,"y":y,"width":width,"height":height})
          #Draws rectangles around faces
          draw(image,(x,y,width,height))
        #displays image
        cv.ShowImage(image_name, image)
        data[image_name]=temp
    return data

def draw(image,(x,y,width,height)):
  pt1 = (int(x * IMAGE_SCALE), int(y * IMAGE_SCALE))
  pt2 = (int((x + width) * IMAGE_SCALE), int((y + height) * IMAGE_SCALE))
  cv.Rectangle(image, pt1, pt2, cv.RGB(255, 0, 0), 3, 8, 0)


def main():
  parser = argparse.ArgumentParser(description="#WAT")
  parser.add_argument('files', nargs='*')
  parser.add_argument('--cascade', dest='cascade', default=HAAR_TRAINER, help='Haar cascade file, default %default')
  pargs = parser.parse_args()

  print(json.dumps(procImag(pargs.files,pargs.cascade)))
  if RENDER_IMAGES:
    cv.WaitKey(0)
    for file in pargs.files:
      cv.DestroyWindow(file)

if __name__ == "__main__":
  main()
