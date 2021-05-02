import cv2
from keras.models import model_from_json
from keras.preprocessing.image import img_to_array,load_img
import numpy as np
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

cascade_path="/Users/murakamikei/opt/anaconda3/pkgs/libopencv-3.4.2-h7c891bd_1/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"

model=model_from_json(open("categorize/dataset/train.json").read())

model.load_weights("categorize/dataset/train.hdf5")

cat=["植芝盛平","三船久蔵","國井善弥"]
test_image=("categorize/dataset/test.jpg")
cascade=cv2.CascadeClassifier(cascade_path)
image=cv2.imread(test_image)
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
facerect=cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1,minSize=(10,10))

x=facerect[0][0]
y=facerect[0][1]
w=facerect[0][2]
h=facerect[0][3]

face=gray[y:y+h,x:x+w]
face=cv2.resize(face,(128,128))
save_path="categorize/dataset/check.jpg"
cv2.imwrite(save_path,face)

img=load_img(save_path)
x=img_to_array(img)
x=np.expand_dims(x,axis=0)

f=model.predict(x)
if f[0,0]==1:
    print("植芝盛平だと思われます")
elif f[0,1]==1:
    print("三船久蔵だと思われます")
elif f[0,2]==1:
    print("國井善弥だと思われます")