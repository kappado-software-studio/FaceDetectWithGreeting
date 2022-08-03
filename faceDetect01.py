#face_detect.py
# -*- coding:utf-8 -*-

import os
import cv2
import numpy as np

#keyword ='花澤香菜'
#keyword ='佐倉綾音'
#keyword ='東山奈央'
#keyword =u'ジャニーズ'

#keyword ='ブログ 花澤香菜'
#keyword ='ブログ 佐倉綾音'
#keyword ='ブログ 東山奈央'
#keyword ='ブログ AKB48'
#keyword ='ブログ ジャニーズ'

keyword ='miyuki'


# 先ほど集めてきた画像データのあるディレクトリ
input_data_path = './zuckerberg_images/zuckerberg'
#input_data_path = './'+keyword+'/'+keyword+str(counter)+pal

# 切り抜いた画像の保存先ディレクトリ(予めディレクトリを作っておいてください)
save_path = './cutted_zuck_images/'
# OpenCVのデフォルトの分類器のpath。(https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xmlのファイルを使う)
#cascade_path = './opencv/data/haarcascades/haarcascade_frontalface_default.xml'
#faceCascade = cv2.CascadeClassifier(cascade_path)
cascade_file = "/usr/local/Cellar/opencv/3.4.2/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascade_file)


# 収集した画像の枚数(任意で変更)
image_count = 110
# 顔検知に成功した数(デフォルトで0を指定)
face_detect_count = 0

# 集めた画像データから顔が検知されたら、切り取り、保存する。
for i in range(image_count):
    img_filename = './'+keyword+'/'+keyword+str(i)+'.jpg'
    print ('img_file'+str(i)+':'+img_filename)
    if not os.path.exists(img_filename):
        print (str(i)+':'+img_filename+':'+'NotExist')
        continue


    img = cv2.imread(img_filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = faceCascade.detectMultiScale(gray, 1.1, 3)
    if len(face) > 0:
        for rect in face:
            # 顔認識部分を赤線で囲み保存(今はこの部分は必要ない)
            # cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0,255), thickness=1)
            # cv2.imwrite('detected.jpg', img)
            x = rect[0]
            y = rect[1]
            w = rect[2]
            h = rect[3]
            savefile =  './'+keyword+'/face_'+keyword+str(face_detect_count)+'.jpg'
            print ('savefile'+str(face_detect_count)+':'+savefile)

            cv2.imwrite(savefile, img[y:y+h, x:x+w])
            face_detect_count = face_detect_count + 1

    else:
      print (img_filename+':NoFace')
