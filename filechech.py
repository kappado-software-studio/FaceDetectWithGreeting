# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import sys
import time
import subprocess
import imghdr
import os.path
import shutil
import eval2
import subprocess
import os.path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

#target_dir = "/Users/yone/Dropbox/Public/catch"
target_dir = "/Users/yone/Dropbox/アプリ/IP Cam Assistant/IUK_5_A1/HVC-089082-DDBDF/2018_08_11/Alarm"
moved_dir = "/Users/yone/Dropbox/Public/catch/moved"

def dispfile(filename):
        print('%sが対象かどうかを思う' %filename)
        #filetype = filecheck_jpg(filename)
        root, ext = os.path.splitext(filename)
        print('ファイル形式は%sです。' % ext)
        if ext=='.jpg':
            chkfile(filename)

def mvfile(filename):
        print('%sをMoveしようと思う' %filename)
        mvs = target_dir + '/' + filename
        mvd = moved_dir + '/' + filename
        print('%sをMove元' %mvs)
        print('%sをMove先' %mvd)
        shutil.move(mvs,mvd)

def chkfile(filename):
        mvs = target_dir + '/' + filename
        print('%sをcheckしようと思う' %mvs)
        # eval.pyへアップロードされた画像を渡す
        result = eval2.evaluation(mvs, './model2.ckpt')
        print('----------------')
        if result != []:
            print(result)
            #print(result[0][0].name)
            print(result[0][0]['name'])
            print(result[0][0]['rate'])
            rate = int(result[0][0]['rate'])
            cmd = ''
            if rate > 80.0:
                names = result[0][0]['name']
                print(names)
                if names == 'miyuki':
                    cmd = 'curl -X GET http://192.168.119.4:8091/google-home-notifier?text=miyuki+san+ohayougozaimasu'
                    req = os.system(cmd)
                    #returncode = subprocess.Popen(cmd)
                else:
                    cmd = 'curl -X GET http://192.168.119.4:8091/google-home-notifier?text=manabu+san+ohayougozaimasu'
                    req = os.system(cmd)
                    #returncode = subprocess.Popen(cmd)


        print('----------------')
        mvfile(filename)

class ChangeHandler(FileSystemEventHandler):

    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%sができました' % filename)
        dispfile(filename)

    def on_modified(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%sを変更しました' % filename)
        dispfile(filename)


    def on_deleted(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%sを削除しました' % filename)



if __name__ in '__main__':
    while 1:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, target_dir, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
