# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:01:03 2019

@author: Marcus
"""
from ffmpeg import *
import numpy as np
import os
files=[]
def Traversal():
    path ='d:\\'
    f_list = os.listdir(path)
    for file in f_list:
        if os.path.splitext(file)[-1] =='.mkv':
            files.append(file)
Traversal()
files=np.unique(files)
path = 'd:\\'
for file in files:
    path1 = os.path.join(path,file)
    path2 = os.path.join(path,file[0:-3]) + 'mp4'
    ff=ffmpeg(inputs ={path1:None},
                     outputs={path2:None}
              )
    ff.cmd
    ff.run()
print('666')