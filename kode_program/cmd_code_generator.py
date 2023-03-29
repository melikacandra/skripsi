# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 21:19:05 2023

@author: Melika
"""

import os
path = 'C:\Melika\images\images'
file_list = os.listdir(path)
file_num_list = []
for value in file_list:
    value2 = value.replace(".jpg","")
    file_num_list.append(value2)
    

g_cloud_script = "gcloud ml vision detect-text "
path_source =  'C:\Melika\images\images\\'
#file_name = ...
jpg = ".jpg"
path_destination = " > C:\Melika\Skripsi\hasil_cloud_vision_api\\"
#file_name = ....
json = ".json"
script = "gcloud ml vision detect-text C:\Melika\images\images\0.50.jpg > C:\Melika\Skripsi\hasil_cloud_vision_api\0.50.json"  
tes = ""
for file_name in file_num_list:
    command=g_cloud_script+path_source+file_name+jpg+path_destination+file_name+json+" & "
    tes = tes + command
print(tes)
