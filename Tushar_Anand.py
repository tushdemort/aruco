#Please download the dictionaries.py as well, without it this code will NOT run
import cv2
import cv2.aruco as aru 
from dictionaries import dict
import numpy

def naming(location_temp,id,img):
    location=[0,0]
    location[0]=int(location_temp[0])+ 3
    location[1]=int(location_temp[1])+3
    location=tuple(location)
    id=int(id)
    text='ID='+str(id)
    cv2.putText(img,text,location, cv2.FONT_HERSHEY_COMPLEX,0.5,color = (0, 0, 255))

def detect(name):
    for i in dict:
        aruco_dict = aru.getPredefinedDictionary(i)
        aruco_param = aru.DetectorParameters()
        detector = aru.ArucoDetector(aruco_dict, aruco_param)
        img = cv2.imread(name)
        markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(img)
        if markerIds is None:
            continue
        else:
            #aru.drawDetectedMarkers(img, markerCorners, markerIds )
            aru.drawDetectedMarkers(img, markerCorners)
            for i in range(len(markerIds)):
                naming(markerCorners[i][0][0],markerIds[i][0],img)
            cv2.imshow('miage',img)
            cv2.waitKey(0)

detect("aruco.png" )
