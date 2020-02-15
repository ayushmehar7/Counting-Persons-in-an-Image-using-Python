import numpy as np
import matplotlib.pyplot as plt
import cv2
from mtcnn import MTCNN
detector = MTCNN()
img = cv2.imread("PATH")
result = detector.detect_faces(img)
print("The imported picture contains {} perons".format(len(result)))
def show_faces(result):
    for i in range(len(result)):
        x1, y1, width, height = result[i]['box']
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + width, y1 + height
        pic = cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),5)
    return pic
pic = show_faces(result)
pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
plt.imshow(pic)

