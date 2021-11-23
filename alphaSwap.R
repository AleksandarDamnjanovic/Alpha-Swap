#*****************************
#Title: Alpha Swap
#Author: Aleksandar Damjanovic
#Date: 22.11.2021
#*****************************

library("readr")
library("officer")
library("pdftools")

alphaSwap_init<- function() {
  d<-read.csv('dictionary.csv')
  nm<-c('1','2')
  f<-data.frame('1'='A', '2'='A')
  colnames(d)<-nm
  colnames(f)<-nm
  dd<-rbind(f,d)
  return(dd)
}

parseRaw<-function(string){
  vec<-strsplit(string,"")
  vec<-as.vector(vec)
  vec1<-''
  for(i in 1:length(vec)){
    let<- dict$`2`[dict$`1`==vec[[1]][i]]
    if(length(let)=='NA'){
      let<- as.character(let)
      vec1<- paste(vec1, let, sep = "")
    }else{
      vec1<-paste(vec1, string[i], sep = "")
    }
  }
  vec1<-as.character(vec1)
  return(vec1)
}

parseTxt<-function(path){
  if(endsWith(path,'txt')!=TRUE){
    stop('txt extension is mandatory')
  }else{
    string<-read_file(path)
    content<-parseRaw(string)
    newPath<-paste('swap_', path)
    write_file(content, newPath, append = FALSE)
  }
}

parseWord<-function(path){
  dict<-alphaSwap_init()
  path<-'test.docx'
  content<-read_docx(path)
  content<-docx_summary(content)
  content<-content$text
  newPath<-paste('swap_', path, ".txt")
  if(file.exists(newPath))
    file.remove(newPath)
  for(i in 1:length(content)){
    t<- as.character(content[i])
    trans<-parseRaw(t)
    write_file(trans, newPath, append = TRUE)
    write_file('\n', newPath, append = TRUE)
  }
}

parsePdf<-function(path){
  pdf<-pdf_text(path)
  newPath<-paste('swap_', path, ".txt")
  if(file.exists(newPath))
    file.remove(newPath)
  for(i in 1:length(pdf)){
    trans<-parseRaw(pdf[i])
    write_file(trans, newPath, append = TRUE)
    write_file('\n', newPath, append = TRUE)
  }
}

parseDir<-function(path){
  path<-"./"
  
  files<-list.files(path,pattern = "*.txt")
  for(i in files){
    parseTxt(i)
  }
  
  files<-list.files(path,pattern = "*.docx")
  for(i in files){
    parseWord(i)
  }
  
  files<-list.files(path,pattern = "*.pdf")
  for(i in files){
    parsePdf(i)
  }
  
}