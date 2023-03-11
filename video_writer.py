import cv2 
import numpy as np
 
cap = cv2.VideoCapture(0)
 
if (cap.isOpened() == False): 
  print("Can not open camera")
 
f_width = int(cap.get(3))
f_height = int(cap.get(4))
 
# Implementing the MJPG codec  
out = cv2.VideoWriter('result.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (f_width,f_height))
 
while(True):
  ret, frame = cap.read()
  
  if ret == True: 
     
    # Write the frame into file 
    out.write(frame)
 
    # Display the result frame   
    cv2.imshow('frame',frame)
 
    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break
     
  
  else:
    break 
 
cap.release()
out.release()
 
# Closes all frames
cv2.destroyAllWindows()