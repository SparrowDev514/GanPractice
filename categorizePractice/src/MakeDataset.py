from keras.preprocessing.image import array_to_img,img_to_array,load_img
import numpy as np
import os

X_train=[]
Y_train=[]

X_test=[]
Y_test=[]

data=os.listdir("/Users/murakamikei/Desktop/pracCategorize/myDataSets/martial")
for row in data:
    i=os.listdir("/Users/murakamikei/Desktop/pracCategorize/myDataSets/martial/"+row)
    n=0
    for target_file in i:
        image=("/Users/murakamikei/Desktop/pracCategorize/myDataSets/martial/"+row+"/"+target_file)
        if n>5:
            temp_img=load_img(image)
            temp_img_array=img_to_array(temp_img)
            X_train.append(temp_img_array)
            Y_train.append(row.split(".")[0])
            n=n+1
        else:
            temp_img=load_img(image)
            temp_img_array=img_to_array(temp_img)
            X_test.append(temp_img_array)
            Y_test.append(row.split(".")[0])
            n=n+1

np.savez("/Users/murakamikei/Desktop/pracCategorize/myDataSets/mydatasets.npz",x_train=X_train,y_train=Y_train,x_test=X_test,y_test=Y_test)