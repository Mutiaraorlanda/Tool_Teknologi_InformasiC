# Python program to demonstrate erosion and
# dilation of images.
import cv2
import numpy as np
from tkinter import filedialog
from tkinter import*
from PIL import Image, ImageTk
from subprocess import call
from tkinter import simpledialog
from tkinter.filedialog import askopenfile
from tkinter import ttk
import matplotlib.pyplot as plt

root = Tk()
root.title("astungkara")
ukurangambar = (200,200)

gambarmasuk, converting = dict(), dict()

def box(): #untuk mendeklarasikan box tempat gambar beroperasi
   
    imgconvert = Image.new("RGB", ukurangambar)
    converting["image"] = ImageTk.PhotoImage(imgconvert)

    labelgambarasli = Label(root, image= converting["image"])
    labelgambarasli.grid(row= 1, column=1)

    labelopening = Label(root, image= converting["image"])
    labelopening.grid(row=1, column=2)
    
    labeldilasi = Label(root, image= converting["image"])
    labeldilasi.grid(row=1, column=3)

    labelerosi = Label(root, image= converting["image"])
    labelerosi.grid(row=1, column=4)

    labelthinning = Label(root, image= converting["image"])
    labelthinning.grid(row=1, column=5)

    labelclosing = Label(root, image= converting["image"])
    labelclosing.grid(row=1, column=6)

box()

def open_image():
    # path= filedialog.askopenfilename(title="Open Image", filetype=(('image files','*.png'),('all files','*.*')))
    # img = cv2.imread(path)

    global imageinput
    root.imagefile = filedialog.askopenfilename(initialdir="", filetypes=(("png files", "*.png *.jpg *.jpeg"), ("all files", "*.*")))
    fileadress = root.imagefile

    #TEMPAT FOTO YANG DIUNGGAH 
    imageinput = Image.open(fileadress).resize((ukurangambar))
    gambarmasuk["image"] = ImageTk.PhotoImage(imageinput)
    tombolInputGambar = Label(root, image=gambarmasuk["image"])
    tombolInputGambar.grid(row=1, column=1)

# def minta_kernel():
#     global img_erosion, img_dilation, img_opening, img_closing, kernel
#     ans=simpledialog.askinteger("input nilai kernel", "Masukkan Konstanta Kernel Matriks", parent=Tk())
#     b=int(ans)
#     kernel =  cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(b,b))

def operasi():
    global img_erosion, img_dilation, img_opening, img_closing, kernel
    ans=simpledialog.askinteger("input nilai kernel", "Masukkan Konstanta Kernel Matriks", parent=Tk())
    b=int(ans)
    kernel =  cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(b,b))
    option=isi.get()

    if option == 1 :
        img_erosion = cv2.erode(imageinput, kernel)
    elif option == 2 : 
        img_dilation = cv2.dilate(imageinput, kernel, iterations=1)
    elif option == 3 : 
        # img_thinning=cv2.ximgproc.thinning(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY))
        img_opening = cv2.morphologyEx(imageinput, cv2.MORPH_OPEN, kernel)
        img_closing = cv2.morphologyEx(imageinput, cv2.MORPH_CLOSE, kernel)

# LABEL (DEKLARASI LABEL)
label1 = Label(root, text = "Gambar Asli")
label1.grid(row= 0, column= 1)
label2 = Label(root, text = "Opening")
label2.grid(row= 0, column= 2)
label3 = Label(root, text = "Dilasi")
label3.grid(row = 0, column= 3)
label4 = Label(root, text = "Erosi")
label4.grid(row = 0, column= 4)
label5 = Label(root, text = "Thinning")
label5.grid(row = 0, column= 5)
label6 = Label(root, text = "Closing")
label6.grid(row= 0, column= 6)


#### TOMBOL / BUTTON ####
#BUTTON UNTUK BUKA FILE (DEKLARASI BUTTON)
tombolInputGambar = Button(root, text="Buka File", command=open_image)
tombolResetGambar = Button(root, text="Reset", command=box)

#GRID BUTTON (UNTUK MENAMPILKAN BUTTON)
tombolInputGambar.grid(row=3, column=1,sticky=EW) #EW : EAST WEST
tombolResetGambar.grid(row=3, column=3,sticky=EW)

isi = IntVar() 

#### CHECKBOX ####
#CHECKBOX (DEKLARASI CHECKBOX)
Centangdilasi= ttk.Radiobutton(root, text="DILASI", variable=isi, value=1, command= operasi)
Centangerosi = ttk.Radiobutton(root, text="EROSI", variable=isi, value=2,command= operasi)
Centangthinning = ttk.Radiobutton(root, text="THINNING", variable=isi, value=3,command= operasi)

#GRID CHECKBOX (NAMPILIN CHECKBOX)
Centangdilasi.grid (row= 2, column= 4, sticky=EW)
Centangerosi.grid (row= 3, column= 4, sticky=EW)
Centangthinning.grid (row= 4, column= 4, sticky=EW)

# fig, ax = plt.subplots(ncols=3, nrows=2)
# global imageinput
# ax[0,0].imshow(imageinput)
# ax[0,1].imshow(img_erosion)
# ax[0,2].imshow(img_dilation)
# # ax[1,0].imshow(img_thinning)
# ax[1,1].imshow(img_closing)
# ax[1,2].imshow(img_opening)

# plt.show()
cv2.waitKey(0)
root.mainloop()

