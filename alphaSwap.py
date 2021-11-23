'''
Created by Aleksandar Damnjanovic
Date: 13.11.2021
Last edit: 22.11.2021
'''

from io import FileIO
import os
import docx2txt
import pdfplumber
import string

class alphaSwap:

    def __init__(self) -> None:
        self.d= self.parseCSV()

    def parseCSV(self):
        file= open('dictionary.csv', 'r')
        content= file.read()
        content=content.split('\n')
        _d= dict()
        for dd in content:
            dd= dd.split(',')
            _d[dd[0]]= dd[1]
        return _d

    def swapRawText(self, text):
        letter=""
        for c in text:
            try:
                letter+=str(self.d[c])
            except:
                letter+=str(c)
        return letter

    def swapTextFile(self, path):
        file= open(path, "r")
        text= file.read()
        file.close()
        t= self.swapRawText(text)
        fname= os.path.basename(path)
        nname= "swap_"+fname+".txt"
        fpath= str.replace(path, fname,"")
        npath=fpath+nname
        file= open(npath,"w")
        file.write(t)
        file.close()
        print("swap completed")
        
    def swapDocxFile(self, path):
        text= docx2txt.process(path)
        t= self.swapRawText(text)
        fname= os.path.basename(path)
        nname= "swap_"+fname+".txt"
        fpath= str.replace(path, fname,"")
        npath=fpath+nname
        file= open(npath,"w")
        file.write(t)
        file.close()
        print("swap completed")

    def swapPdfFile(self, path):
        text= pdfplumber.open(path)

        t=''
        for p in text.pages:
            t+= self.swapRawText(p.extract_text())

        fname= os.path.basename(path)
        nname= "swap_"+fname+".txt"
        fpath= str.replace(path, fname,"")
        npath=fpath+nname
        file= open(npath,"w")
        file.write(t)
        file.close()
        print("swap completed")

    def processDirectory(self, path):
        l=os.listdir(path)
        d=''
        for file in l:
            if d=='':
                d= str.replace(os.path.abspath(path), file, "")
                if str.endswith(d,"/")!=True:
                    d+=os.sep
                 
            if (d+file).endswith(".pdf"):
                self.swapPdfFile(d+file)
            elif (d+file).endswith(".docx"):
                self.swapDocxFile(d+file)
            elif (d+file).endswith(".txt"):
                self.swapTextFile(d+file)