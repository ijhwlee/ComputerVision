import sys
import cv2
sys.path.append('d:\\Lec_hwlee\\ComputerVision\\y2024\\sources')
#print(sys.path)
from Common.utils import put_string

capture = cv2.VideoCapture(1)
if capture.isOpened() == False:
    raise Exception("카메라연결 안됨")
print(f"너비 {capture.get(cv2.CAP_PROP_FRAME_WIDTH)}")
print(f"높이 {capture.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
print(f"노출 {capture.get(cv2.CAP_PROP_EXPOSURE)}")
print(f"밝기 {capture.get(cv2.CAP_PROP_BRIGHTNESS)}")

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >=0: break
    exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
    put_string(frame, 'EXPOS: ', (10, 40), exposure)
    title = "View Frame from Camera"
    cv2.imshow(title, frame)
    
capture.release()