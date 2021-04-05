import cv2
import os

cascade_path = "/Users/murakamikei/opt/anaconda3/pkgs/libopencv-3.4.2-h7c891bd_1/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"

X_train = []
Y_train = []

X_test = []
Y_test = []

l = os.listdir("categorizePractice/myDataSets/inputFile")
for i in l:
    result_dir = i.split(".")[0]
    os.mkdir("categorizePractice/myDataSets/martial/" + result_dir)
    m = os.listdir("categorizePractice/myDataSets/inputFile/" + i)
    n = 0
    for target_file in m:
        origin_image = ("categorizePractice/myDataSets/inputFile/" + i + "/" + target_file)
        print("origin_image",origin_image)
        cascade = cv2.CascadeClassifier(cascade_path)
        image = cv2.imread(origin_image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        facerect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(10, 10))

        for x, y, w, h in facerect:
            face = gray[y:y + h, x:x + w]
            face = cv2.resize(face, (128, 128))
            save_path = "categorizePractice/myDataSets/martial/" + result_dir + "/image_" + str(n) + ".jpg"
            cv2.imwrite(save_path, face)
            n = n + 1
            face = cv2.flip(face, 1)
            save_path = "categorizePractice/myDataSets/martial/" + result_dir + "/image_" + str(n) + ".jpg"
            cv2.imwrite(save_path, face)
            n = n + 1
            face = cv2.blur(face, (10, 10))
            save_path = "categorizePractice/myDataSets/martial/" + result_dir + "/image_" + str(n) + ".jpg"
            cv2.imwrite(save_path, face)
            n = n + 1
            face = cv2.blur(cv2.flip(face, 1), (10, 10))
            save_path = "categorizePractice/myDataSets/martial/" + result_dir + "/image_" + str(n) + ".jpg"
            cv2.imwrite(save_path, face)
            n = n + 1
