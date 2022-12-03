import cv2
import numpy as np
from tkinter import filedialog
from tkinter import*
from PIL import Image, ImageTk
from subprocess import call
from tkinter import simpledialog
import matplotlib.pyplot as plt
import mahotas
import mahotas.demos


path= filedialog.askopenfilename(title="Pilih Gambar", filetype=(('image files','*.png'),('all files','*.*')))
img = cv2.imread(path)

ans=simpledialog.askinteger("Input Nilai Kernel", "Masukkan Konstanta Kernel Matriks", parent=Tk())
b=int(ans)
kernel =  cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(b,b))


img_erosion = cv2.erode(img, kernel)
img_dilation = cv2.dilate(img, kernel, iterations=1)


gambar=img.max(2)
skel=mahotas.otsu(gambar)
gambar=gambar>skel
img_thinning=mahotas.thin(gambar)

img_opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img_closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


fig, ax = plt.subplots(ncols=3, nrows=2)
ax[0,0].imshow(img)
ax[0,1].imshow(img_erosion)
ax[0,2].imshow(img_dilation)
ax[1,0].imshow(img_thinning)
ax[1,1].imshow(img_closing)
ax[1,2].imshow(img_opening)

ax[0,0].annotate('GAMBAR ASLI', 
    (1, 1), # these are the coordinates to position the label
    color='blue') # you can pass any extra params too

ax[0,1].annotate('EROSI', 
    (1, 1), # these are the coordinates to position the label
    color='blue') # you can pass any extra params too

ax[0,2].annotate('DILASI', 
    (1, 1), # these are the coordinates to position the label
    color='blue') # you can pass any extra params too

ax[1,0].annotate('THINNING', 
    (1, 1), # these are the coordinates to position the label
    color='blue') # you can pass any extra params too

ax[1,1].annotate('CLOSING', 
    (1, 1), # these are the coordinates to position the label
    color='blue') # you can pass any extra params too

ax[1,2].annotate('OPENING', 
    (1, 1), # these are the coordinates to position the label
    color='blue') # you can pass any extra params too

plt.show()
cv2.waitKey(0)


