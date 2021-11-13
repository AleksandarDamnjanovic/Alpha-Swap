'''
Created by Aleksandar Damnjanovic
Date: 13.11.2021
'''

from io import FileIO
import dictionaries as d
import os
import docx2txt
import pdfplumber
import string

class alphaSwap:

    @staticmethod
    def swapRawText(text):
        letter=""
        for c in text:
            try:
                letter+=str(d.base[c])
            except:
                letter+=str(c)
        return letter

    @staticmethod
    def swapTextFile(path):
        file= open(path, "r")
        text= file.read()
        file.close()
        t= alphaSwap.swapRawText(text)
        fname= os.path.basename(path)
        nname= "swap_"+fname+".txt"
        fpath= str.replace(path, fname,"")
        npath=fpath+nname
        file= open(npath,"w")
        file.write(t)
        file.close()
        print("swap completed")
        
    @staticmethod
    def swapDocxFile(path):
        text= docx2txt.process(path)
        t= alphaSwap.swapRawText(text)
        fname= os.path.basename(path)
        nname= "swap_"+fname+".txt"
        fpath= str.replace(path, fname,"")
        npath=fpath+nname
        file= open(npath,"w")
        file.write(t)
        file.close()
        print("swap completed")

    @staticmethod
    def swapPdfFile(path):
        text= pdfplumber.open(path)
        t= alphaSwap.swapRawText(text.pages[0].extract_text())
        fname= os.path.basename(path)
        nname= "swap_"+fname+".txt"
        fpath= str.replace(path, fname,"")
        npath=fpath+nname
        file= open(npath,"w")
        file.write(t)
        file.close()
        print("swap completed")

    @staticmethod
    def processDirectory(path):
        l=os.listdir(path)
        d=''
        for file in l:
            if d=='':
                d= str.replace(os.path.abspath(path), file, "")
                if str.endswith(d,"/")!=True:
                    d+=os.sep
                 
            if (d+file).endswith(".pdf"):
                alphaSwap.swapPdfFile(d+file)
            elif (d+file).endswith(".docx"):
                alphaSwap.swapDocxFile(d+file)
            elif (d+file).endswith(".txt"):
                alphaSwap.swapTextFile(d+file)