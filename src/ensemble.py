import cv2
import sys
from PIL import Image
import numpy as np
from algorithms import N4, N8, WS

#for f1 and f2
#load input
ipt = np.loadtxt(open("../input/f1_dinv.txt"), delimiter = ",")
opt_N4 = WS(ipt, N4)
opt_N8 = WS(ipt, N8)
np.savetxt("../output/f1_dinv_wt_4.txt", opt_N4, fmt = '%d', delimiter = ',', newline = '\n')
np.savetxt("../output/f1_dinv_wt_8.txt", opt_N8, fmt = '%d', delimiter = ',', newline = '\n')

ipt = np.loadtxt(open("../input/f2.txt"), delimiter = ",")
opt_N4 = WS(ipt, N4)
opt_N8 = WS(ipt, N8)
np.savetxt("../output/f2_wt_4.txt", opt_N4, fmt = '%d', delimiter = ',', newline = '\n')
np.savetxt("../output/f2_wt_8.txt", opt_N8, fmt = '%d', delimiter = ',', newline = '\n')

#for 3 self images

ipt1 = cv2.imread("../input/f3.png", 0)
ipt1 = cv2.medianBlur(ipt1, 5)
ipt1 = cv2.bilateralFilter(ipt1, 19, 75, 75)
ipt1 = cv2.adaptiveThreshold(ipt1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)

ipt2 = cv2.imread("../input/f4.png", 0)
ipt2 = cv2.bilateralFilter(ipt2, 5, 75, 75)
ipt2 = cv2.medianBlur(ipt2, 23)  
ipt2 = cv2.bitwise_not(ipt2)

ipt3 = cv2.imread("../input/f5.png", 0)
ipt3 = cv2.medianBlur(ipt3, 5)  
ipt3 = cv2.adaptiveThreshold(ipt3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 3)

def arr_to_im(opt, name):
        im = Image.fromarray(opt)
        cv2.imwrite(name, opt)

opt1 = WS(ipt1, N8)
opt2 = WS(ipt2, N8)
opt3 = WS(ipt3, N8)

arr_to_im(ipt1, "../output/f3_seg.png")
arr_to_im(opt1, "../output/f3_wt_8.png")
np.savetxt("../output/f3_wt_8.txt", ipt1, fmt='%d', delimiter=',', newline='\n', header='', footer='', comments='# ', encoding=None)

arr_to_im(ipt2, "../output/f4_seg.png")
arr_to_im(opt2, "../output/f4_wt_8.png")
np.savetxt("../output/f4_wt_8.txt", ipt2, fmt='%d', delimiter=',', newline='\n', header='', footer='', comments='# ', encoding=None)

arr_to_im(ipt3, "../output/f5_seg.png")
arr_to_im(opt3, "../output/f5_wt_8.png")
np.savetxt("../output/f5_wt_8.txt", ipt3, fmt='%d', delimiter=',', newline='\n', header='', footer='', comments='# ', encoding=None)