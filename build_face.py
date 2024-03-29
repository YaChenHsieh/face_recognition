# import the necessary packages
from imutils.video import VideoStream
from imutils import face_utils
import argparse
import imutils
import time
import dlib
import cv2
from load_face import Loadface


class Build_face:
    
    def run_cam(self,vs):
        #construct the argument parser and parse the arguments
        #ap = argparse.ArgumentParser()
        #ap.add_argument("-p", "--shape-predictor", required=True,
        #    help="path to facial landmark predictor")
        #args = vars(ap.parse_args())
        # initialize dlib's face detector (HOG-based) and then create the
        
        # facial landmark predictor
        print("[INFO] loading facial landmark predictor...")
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor('face_landmarks_5points.dat')
        
        
        #user insert name
        name = input('Please insert your name:')
        
        
        while True:
            # grab the frame from the threaded video stream, resize it to
            # have a maximum width of 400 pixels, and convert it to
            # grayscale
            frame = vs.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         
            # detect faces in the grayscale frame
            rects = detector(gray, 0)
            
            # check to see if a face was detected, and if so, draw the total
            # number of faces on the frame
            if len(rects) > 0:
                text = "{} face(s) found".format(len(rects))
                cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 2)
                if len(rects)>1:
                    text = 'Please keep one face inside the frame'
                    cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 2)

        
            # loop over the face detections
            for rect in rects:
                # compute the bounding box of the face and draw it on the
                # frame
                (bX, bY, bW, bH) = face_utils.rect_to_bb(rect)
                cv2.rectangle(frame, (bX, bY), (bX + bW, bY + bH),
                    (0, 255, 0), 1)
        
                # determine the facial landmarks for the face region, then
                # convert the facial landmark (x, y)-coordinates to a NumPy
                # array    
                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)
         
                # loop over the (x, y)-coordinates for the facial landmarks
                # and draw each of them
                for (i, (x, y)) in enumerate(shape):
                    cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
                    cv2.putText(frame, str(i + 1), (x - 10, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
        
            # show the frame
            cv2.imshow("Video", frame)
            key = cv2.waitKey(1) & 0xFF
        
        
            #if found only 1 face, and type in q
            if (len(rects) == 1) and (key == ord('p')):
                cv2.imwrite('/home/angel/Desktop/donkey_custom/angel_facerec/face_photo/{}.jpg'.format(name),frame)
                print('face in and crop:{}'.format(name))
        
                cv2.rectangle(frame,(50,50),(300,110),(0,0,0),-1)
                text = 'Cropped'
                cv2.putText(frame, text,(50,100), cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),3)
                cv2.imshow('Video',frame)
                key = cv2.waitKey(1) & 0xFF
        
                load = Loadface()
                load.load_json()
                load.update(name)
                load.to_json()
                
                time.sleep(3)
                break
        
        
        
        
            # if the `q` key was pressed, break from the loop   
            elif key == ord("q"):
                break
        
        # do a bit of cleanup
        cv2.destroyAllWindows()
        vs.stop()

if __name__ =='__main__':

    build = Build_face()
    build.run_cam()

