from typing import List, Optional
import cv2 as cv

f = 'C://Users//daijitao//Desktop//yemei.png'
outf = 'C://Users//daijitao//Desktop//yemei1.png'

img = cv.imread(f, 0)
cv.imshow("1", img)
cv.waitKey(0)
