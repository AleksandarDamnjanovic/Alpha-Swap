#*****************************
#Title: Alpha Swap
#Author: Aleksandar Damjanovic
#Date: 23.11.2021
#*****************************

source('alphaSwap.R', chdir = TRUE)

args= commandArgs(trailingOnly = TRUE)

if(length(args)==0){
  stop('You must provide an input in order for script to continue.')
}else{
  dict<-alphaSwap_init()
  
  if(args[1]== '-raw' && length(args)>1){
    raw<-parseRaw(args[2])
    print(raw)
  }else if(args[1]=='-txt' && length(args)>1){
    parseTxt(args[2])
  }else if(args[1]=='-doc' && length(args)>1){
    parseWord(args[2])
  }else if(args[1]=='-pdf' && length(args)>1){
    parsePdf(args[2])
  }else if(args[1]=='-dir' && length(args)>1){
    parseDir(args[2])
  
}