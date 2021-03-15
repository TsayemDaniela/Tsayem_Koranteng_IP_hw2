import numpy as np
from algorithms import N4, N8, WS
import sys
import cv2
from PIL import Image

#obtaining input values 
Nx = sys.argv[1]
ipt = sys.argv[2]
opt = sys.argv[3]

#load input
lipt = np.loadtxt(open(ipt), delimiter = ",")

#choosing neighborhoods
if Nx == 4 or Nx == '4':
    lopt = wshed(lipt, N4)

elif Nx == 8 or Nx == '8':
    lopt = wshed(lipt, N8)

np.savetxt(opt, lopt, fmt = '%d', delimiter = ',', newline = '\n')