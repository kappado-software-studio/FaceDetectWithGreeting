#face_detect.py
# -*- coding:utf-8 -*-

import os
import cv2
import numpy as np

src_image='test.jpg'

def main():
    # カスケード型識別器の読み込み
    cascade_file = "/usr/local/Cellar/opencv/3.4.2/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(cascade_file)

    src = cv2.imread(src_image)
    cv2.imwrite("src_img.jpg",src)

    row,col,ch = src.shape
    s_vs_p = 0.5
    amount = 0.004
    sp_img = src.copy()

    # 塩モード
    num_salt = np.ceil(amount * src.size * s_vs_p)
    coords = [np.random.randint(0, i-1 , int(num_salt)) for i in src.shape]
    sp_img[coords[:-1]] = (255,255,255)

    #cv2.imwrite("sp_img",sp_img)

    # 胡椒モード
    num_pepper = np.ceil(amount* src.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i-1 , int(num_pepper)) for i in src.shape]
    sp_img[coords[:-1]] = (0,0,0)

    cv2.imwrite("sp_img2.jpg",sp_img)


    src = cv2.imread(src_image)
    hflip_img = cv2.flip(src, 1)
    vflip_img = cv2.flip(src, 0)

    cv2.imwrite("hflip_img.jpg",hflip_img)
    cv2.imwrite("vflip_img.jpg",vflip_img)

    src = cv2.imread(src_image)
    hight = src.shape[0]
    width = src.shape[1]
    #half_img = cv2.resize(src,(hight/2,width/2))

    #cv2.imwrite("half_img.jpg",half_img)

if __name__ == '__main__':
    main()
