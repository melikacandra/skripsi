# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:09:31 2023

@author: Melika
"""

import json
import os
path = "C:\Melika\Skripsi\hasil_cloud_vision_api\hasil_json"
list_dir = os.listdir(path)
result = []
for file in list_dir:
    f = open(path+"\\"+file)
    data = json.load(f)
    print(file)
    try:
        description = data["responses"][0]['textAnnotations'][0]['description']
    except:
        description = "unknown"
    result.append(description)
    
  
# Closing file
f.close()

#kode untuk cek kebenaran total
import os
path = 'C:\Melika\images\images'
file_list = os.listdir(path)
file_num_list = []
for value in file_list:
    value2 = value.replace(".jpg","")
    file_num_list.append(value2)

file_num_list

eval = 0
for i in range(100):
    if(file_num_list[i]==result[i]):
        eval += 1
    
    
###Hasilnya adalah akurasinya 48%