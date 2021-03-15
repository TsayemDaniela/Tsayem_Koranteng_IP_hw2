import cv2
from PIL import Image
import numpy as np
from function import N4, N8, WS

ipt1 = cv2.imread("../input/f3.png", 0)
ipt1 = cv2.medianBlur(ipt1, 5)
ipt1 = cv2.bilateralFilter(ipt1, 19, 75, 75)
ipt1 = cv2.adaptiveThreshold(ipt1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)

ipt2 = cv2.imread("../input/f4.png", 0)
ipt2 = cv2.bilateralFilter(ipt2, 5, 75, 75)
ipt2 = cv2.medianBlur(ipt2, 23)  
ipt2 = cv2.bitwise_not(ipt2)

ipt3 = cv2.imread("../input/f5.png", 0)
ipt3 = cv2.medianBlur(ipt2, 5)  
ipt3 = cv2.adaptiveThreshold(ipt2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 3)

def to_im(out, name):
        im = Image.fromarray(out)
        cv2.imwrite(name, out)

out1 = watershed(ipt1, neighbor_8)
out2 = watershed(ipt2, neighbor_8)
out3 = watershed(ipt3, neighbor_8)

to_im(inp, "../output/f3_seg.png")
to_im(out, "../output/f3_wt_8.png")
np.savetxt("../output/f3_wt_8.txt", inp, fmt='%d', delimiter=',', newline='\n', header='', footer='', comments='# ', encoding=None)

to_im(inp, "../output/f4_seg.png")
to_im(out, "../output/f4_wt_8.png")
np.savetxt("../output/f4_wt_8.txt", inp, fmt='%d', delimiter=',', newline='\n', header='', footer='', comments='# ', encoding=None)

to_im(inp, "../output/f5_seg.png")
to_im(out, "../output/f5_wt_8.png")
np.savetxt("../output/f5_wt_8.txt", inp, fmt='%d', delimiter=',', newline='\n', header='', footer='', comments='# ', encoding=None)