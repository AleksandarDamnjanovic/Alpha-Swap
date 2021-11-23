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

obj= asw.alphaSwap()

if p!='-raw':
    if a=="":
        try:
            if str.endswith(p,".pdf"):
                obj.swapPdfFile(p)
            elif str.endswith(p, ".docx"):
                obj.swapDocxFile(p)
            elif str.endswith(p, ".txt"):
                obj.swapTextFile(p)
        except:
            print("Problem loading the path. Please, check your arguments")
    elif a=='-dir':
        try:
            obj.processDirectory(p)
        except:
            print("Problem loading the path. Please, check your arguments")
else:
    try:
        text=args[2]
        response= obj.swapRawText(text)
        print(response)
    except:
        print("Error! Please, check your arguments")
