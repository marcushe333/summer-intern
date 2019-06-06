# -*- coding: utf-8 -*-



import numpy as np
class Read_File_Iteration: 
    def __init__(self, path):
        self.path = path
    def __iter__(self):
        for line in open(self.path,'rb'):
            yield line.split()


import os
#################

files=[]
def save_file(path,content):
    f1=open(path+'.txt','wb')
    f1.write(content)
    f1.close()
def Traversal():
    path ='F:\BaiduNetdiskDownload'
    f_list = os.listdir(path)
    for file in f_list:
        if os.path.splitext(file)[-1] =='.srt':
            files.append(file)
Traversal()
files=np.unique(files)
# store the filename needed in list 'files'
##################
path='E:\\test'
for file in files:
    filename= file.split('.')[0]
    path1=os.path.join(path,filename)
    isExists=os.path.exists(path1)
    if not isExists:
        os.makedirs(path1)
######################## create directory for certain movie
    flag=1
    count=1
    for item in open(file,'rb'):
        if flag==1:
            new_name=str(count)
            count+=1
            path2=os.path.join(path1,new_name)
            f1=open(path2+'.txt','wb')
        if flag==2:
            f1.write(item)
            #save_file(path2,item)
        if flag==3:
            f1.write(item)

            #save_file(path2,item)
        if flag==4:
            f1.close()
            flag=0
        flag+=1
