#Marissafy on EC2

All of the backend code for Marissafy, a hack built for the Yahoo! 2013 Hackday. Marissafy is an image detection web application that overlays a picture of Marissa Mayer's face on top of detected faces in an uploaded picture.

##More Info

This code was used to drive the back-end stack of the application, run on an EC2 instance. The python script utilizes a Python port of the C++ based OpenCV to power the image processing. It runs through a pre-trained Haar Cascade trainer, which contains processed data from a variety of faces, to determine which parts of an image can be matched to a face.
