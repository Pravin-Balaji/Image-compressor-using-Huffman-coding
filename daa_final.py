

from huffman import Huffman
from tkinter import *


def imgcomp():
    path = "tiger.bmp"

    h = Huffman(path)
    a = path.split(".")
    outpath = "compressed_"+a[0]+".bin"

    def imgcompress():
        output_path = h.compress_img()
        print("Compressed file path:"+output_path)


    def imgdecompress():
        print("file path:" + outpath)
        decom_path = h.decompress_img(outpath)
        print("Decompressed file path: " + decom_path)

    gap, _ = 0, 0
    root = Tk()
    root.geometry('400x400')
    root.resizable(0, 0)
    root.config(bg='ghost white')
    root.title('COMPRESSOR')

    ##heading
    Label(root, text='FOR IMAGE', font='arial 20 bold', bg='white smoke').pack()
    Label(root, text='KARTHIKEYAN-PRAVIN', font='arial 10 bold', bg='white smoke').pack(side=BOTTOM)

    # Button
    Label(root, text='COMPRESS IMAGE', font='arial 20 bold', bg='white smoke').place(x=25, y=90)
    Button(root, text="SELECT", font='arial 15 bold', command=imgcompress, width=6, bg='orange').place(x=25, y=125)
    Label(root, text='DECOMPRESS IMAGE', font='arial 20 bold', bg='white smoke').place(x=25, y=190)
    Button(root, text="SELECT", font='arial 15 bold', command=imgdecompress, width=6, bg='skyblue').place(x=25, y=225)

    # infinite loop to run program
    root.mainloop()

def txtcomp():
    #file_path = askopenfilename()

    #path = os.path.basename(file_path)

    path = "sample.txt"
    h = Huffman(path)
    a = path.split(".")
    outpath = a[0] + ".bin"

    def txtcompress():
        output_path = h.compress_text()
        print("Compressed file path: " + output_path)

    def txtdecompress():
        decom_path = h.decompress_text(outpath)
        print("Decompressed file path: " + decom_path)

    gap, _ = 0, 0
    root = Tk()
    root.geometry('400x400')
    root.resizable(0, 0)
    root.config(bg='ghost white')
    root.title('COMPRESSOR')

    ##heading
    Label(root, text='FOR TEXT FILE', font='arial 20 bold', bg='white smoke').pack()
    Label(root, text='KARTHIKEYAN-PRAVIN', font='arial 10 bold', bg='white smoke').pack(side=BOTTOM)

    # Button
    Label(root, text='COMPRESS TEXT', font='arial 20 bold', bg='white smoke').place(x=25, y=90)
    Button(root, text="SELECT", font='arial 15 bold', command=txtcompress, width=6, bg='orange').place(x=25, y=125)
    Label(root, text='DECOMPRESS TEXT', font='arial 20 bold', bg='white smoke').place(x=25, y=190)
    Button(root, text="SELECT", font='arial 15 bold', command=txtdecompress, width=6, bg='skyblue').place(x=25, y=225)

    # infinite loop to run program
    root.mainloop()

gap,_=0,0
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('COMPRESSOR')


##heading
Label(root, text = 'COMPRESSOR & DECOMPRESSOR' , font='arial 15 bold' , bg ='white smoke').pack()
Label(root, text ='KARTHIKEYAN-PRAVIN' , font ='arial 10 bold', bg = 'white smoke').pack(side = BOTTOM)




#Button
Label(root, text = 'IMAGE COMPRESSOR' , font='arial 20 bold' , bg ='white smoke').place(x=25, y=90)
Button(root, text = "SELECT" , font = 'arial 15 bold', command = imgcomp, width =6, bg='orange').place(x=25, y=125)
Label(root, text = 'TEXT COMPRESSOR' , font='arial 20 bold' , bg ='white smoke').place(x=25, y=190)
Button(root, text = "SELECT" , font = 'arial 15 bold', command = txtcomp, width =6, bg='skyblue').place(x=25,y=225)


#infinite loop to run program
root.mainloop()