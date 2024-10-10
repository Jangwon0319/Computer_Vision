import numpy as np
import cv2


filename = 'mydata.json'

def writeData():
    name = 'Jane'
    age = 10
    pt1 = (100, 200)
    scores = (80, 90, 50)
    mat1 = np.array([[1.0, 1,5], [2.0, 3.2]], dtype=np.float32)

    fs = cv2.FileStorage(filename, cv2.FILE_STORAGE_WRITE)

    if not fs.isOpened():
        print("File open fail")
        return

    fs.write('name', name)
    fs.write('age', age)
    fs.write('point', pt1)
    fs.write('scores', scores)
    fs.write('data', mat1)

    fs.release()
