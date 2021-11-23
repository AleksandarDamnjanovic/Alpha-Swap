# Alpha Swap

## English
Here you can find simple Python and R tools for the purpose of swapping latinic letters with cirylic ones and vice versa, in txt, docx and pdf files in Serbian language. Also, it's posible to enter raw text through command line and to receive printed output.

### How to use

+ **Python**
    
    + For raw input `run.py -raw "some text to be replaced"`
    + For single file `run.py "path"`
    + For entire content of source directory(in this case, path of a directory should be provided) `run.py "path" -dir`

    Examples:

    + `run.py -raw "swap me"`
    + `run.py "/media/harddrive/file.txt"`
    or `run.py "c:\file.pdf"`
    + `run.py -dir "/media/hardrive/dir"`

+ **R**

    + For raw text `run.R -raw "raw text"`
    + For single file `run.R -txt "file.path"`, `run.R -docx "file path"` or `run.R -pdf "file path"`
    + For directories `run.R -dir "dir path"`


### For developers
`run.py` and `run.R` are scripts for final user. Developer could utilize this packet composed of two files(alphaSwap and dictionary.csv) in some other way. Just forget about `run` and rewrite this
script to fit your purpose.

## Српски
Ово је једноставан алат, написан у Пајтону и Р-у, за сврху измене латиничних карактера у ћирилична и обратно у текстуалним, вордовим и пдф документима на српском језику. Постоји функционалност која омогућава да унесете сиров текст и добијате одштампану измењену верзију истог.

### Како користити
+ **Python**
    
    + За унос сировог текста `run.py -raw "неки текст који ће бити измењен"`
    + За један документ `run.py "путања"`
    + За садржај читавог директоријума(у овом случају треба бити предата путања до директоријума) `run.py "путања" -dir`

    Примери:

    + `run.py -raw "текст за измену"`
    + `run.py "/media/harddrive/file.txt"`
    or `run.py "c:\file.pdf"`
    + `run.py -dir "/media/hardrive/dir"`

+ **R**

    + За сиров текст `run.R -raw "сиров текст"`
    + За један документ `run.R -txt "путања"`, `run.R -docx "путања"` or `run.R -pdf "путања"`
    + За директоријуме `run.R -dir "путања"`

### За софтверске инжењере
`run.py` и `run.R` су скриптови за крајњег корисника. Инжењер може да изкористи овај пакет, састављен од два документа(alphaSwap и dictionaries.csv) на неки други начин. Заборавите на `run` и препишите овај скрип за своју сврху.
