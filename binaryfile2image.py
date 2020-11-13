import binascii
import numpy as np
from PIL import Image



#filepath = "C:\Casa\Peca1.SLDPRT",

def CreateBinaryFromFile(filepath):
    BinFile = open(filepath,'rb',0)
    BinFile = BinFile.read(-1)
    return BinFile

def CreatImageArray(BinData,width=32):
    datalen = len(BinData)
    imageW = width
    imageH = int(datalen/imageW)
    img = Image.new('L',(imageW,imageH))
    imgdata = np.asarray(img)
    imgdata = np.zeros_like(imgdata)
    for i in range(imageH):
        for j in range(imageW):
            datapos = i*imageW+j
            if datapos < datalen:
                imgdata[i][j] = BinData[datapos]
            else:
                imgdata[i][j] = 255
    return imgdata





