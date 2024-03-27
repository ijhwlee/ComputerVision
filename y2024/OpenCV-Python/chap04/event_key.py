import numpy as np 
import cv2

switch_case = {
    ord('v'): "v키 선택",
    ord('w'): "w키 선택",
    ord('x'): "x키 선택",
    ord('y'): "x키 선택",
    0x1B: "ESC키 선택",
    int("4C", 16): "L키 선택"
}

image = np.ones((200,300), np.float32)
cv2.namedWindow("Key Test")
cv2.imshow("Key Test", image)
while True:
    key = cv2.waitKeyEx(00)
    print(f"key = {key}")
    if key == ord('q'): break
    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()

cv2.destroyAllWindows()
