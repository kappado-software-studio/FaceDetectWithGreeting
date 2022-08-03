#
#顔を発見して矩形で囲む
#
import cv2

def main():
    # 入力画像の読み込み
    img = cv2.imread("test.jpg")
    #cv2.imwrite("src_img",img)

    # カスケード型識別器の読み込み
    cascade_file = "/usr/local/Cellar/opencv/3.4.2/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(cascade_file)
    #cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    #src = cv2.imread("test.jpg")
    hflip_img = cv2.flip(img, 1)
    vflip_img = cv2.flip(img, 0)

    cv2.imwrite("hflip_img.jpg",hflip_img)
    #cv2.imwrite("vflip_img",vflip_img)



    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("gray.jpg",gray)
    print('gray')

    # 顔領域の探索
    face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    # 顔領域を赤色の矩形で囲む
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,200), 3)

    # 結果を出力
    cv2.imwrite("result.jpg",img)
    print('End')


if __name__ == '__main__':
    main()
