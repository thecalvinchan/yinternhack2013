#!/usr/bin/python

import cv
import argparse

##Settings

def main():
  parser = argparse.ArgumentParser(description="#WAT")
  parser.add_argument('files', nargs='*')
  args = parser.parse_args()
  data = {}
  procImag(args.files,data)
  print(data)

def procImag(images,data):
  for image in images:
    img = cv.LoadImageM(image,cv.CV_LOAD_IMAGE_GRAYSCALE)
    cascade = cv.Load("haarcascade_frontalface_alt.xml")
    matches = cv.HaarDetectObjects(img,cascade,cv.CreateMemStorage(0),1.2,2,0,(20,20))
    temp = []
    for match in matches:
      temp.append(match[0])
    data[image]=temp

if __name__ == "__main__":
  main()
