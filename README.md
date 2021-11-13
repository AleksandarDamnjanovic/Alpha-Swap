# Alpha Swap

## English
This is a simple python tool for the purpose of swapping latinic letters with cirylic ones and vice versa, in txt, docx and pdf files in Serbian language. Also, it's posible to enter raw text through command line and to receive printed output.

### How to use
For raw input
+ run.py -raw "some text to be replaced"

For single file
+ run.py `path`

For entire content of source directory(in this case, path of a directory should be provided)
+ run.py `path` -dir

### For developers
`run.py` is a script for final user. Developer could utilize this packet composed of two files(alphaSwap.py and dictionaries.py) in some other way. Just forget about run.py and rewrite this
script to fit your purpose.

## Српски
Ово је једноставан алат, написан у пајтону, за сврху измене латиничних карактера у ћирилична и обратно у текстуалним, вордовим и пдф документима на српском језику. Постоји функционалност која омогућава да унесете сиров текст и добијате одштампану измењену верзију истог.

### Како користити
За сиров текст
+ run.py -raw "неки текст који желите да пребаците у друго писмо"

За један документ
+ run.py `путања до циљног документа`

За читав садржај циљаног директоријума(у овом случају путања до директоријума треба да буде предата)
+ run.py `путања до циљног директоријума` -dir

### За софтверске инжењере
`run.py` је скрипт за крајњег корисника. Инжењер може да изкористи овај пакет, састављен од два документа(alphaSwap.py и dictionaries.py) на неки други начин. Заборавите на run.py и препишите овај скрип за своју сврху.