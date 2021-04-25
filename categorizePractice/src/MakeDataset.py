from keras.preprocessing.image import array_to_img,img_to_array,load_img
import numpy as np
from PIL import Image
import os

X_train=[]
Y_train=[]

X_test=[]
Y_test=[]

data=os.listdir("categorizePractice/myDataSets/outputFile/")
for row in data:
    if row == ".DS_Store":
        print("this is .DS_Store")
    elif row == ".gitignore":
        print("this is .gitignore")
    else:
        i=os.listdir("categorizePractice/myDataSets/outputFile/"+row)
        n=0
        for target_file in i:
            image=("categorizePractice/myDataSets/outputFile/"+row+"/"+target_file)
            if target_file == ".DS_Store":
                print('this is DS_Store')
            elif n>5:
                print(image)
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
np.save("categorizePractice/myDataSets/result",X_train,Y_train)
# np.savez("categorizePractice/myDataSets/result.npz",x_train=X_train,y_train=Y_train,x_test=X_test,y_test=Y_test)