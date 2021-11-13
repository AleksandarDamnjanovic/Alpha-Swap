'''
Created by Aleksandar Damnjanovic
Date: 13.11.2021
'''
import alphaSwap as asw
import sys
import string

args= sys.argv

p= args[1]

a=""
if(len(args)>2):
    a= args[2]

if p!='-raw':
    if a=="":
        try:
            if str.endswith(p,".pdf"):
                asw.alphaSwap.swapPdfFile(p)
            elif str.endswith(p, ".docx"):
                asw.alphaSwap.swapDocxFile(p)
            elif str.endswith(p, ".txt"):
                asw.alphaSwap.swapTextFile(p)
        except:
            print("Problem loading the path. Please, check your arguments")
    elif a=='-dir':
        try:
            asw.alphaSwap.processDirectory(p)
        except:
            print("Problem loading the path. Please, check your arguments")
else:
    try:
        text=args[2]
        response= asw.alphaSwap.swapRawText(text)
        print(response)
    except:
        print("Error! Please, check your arguments")