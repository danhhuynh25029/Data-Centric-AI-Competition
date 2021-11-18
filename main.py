import cv2
import glob
import argparse
import imgaug.augmenters as iaa
import os
from get_labels import *
class DataAug:
    def __init__(self):
        self.images_path = None
        self.image = []
        self.aug = None
    def load_images(self,path='*.jpg',c=0,dir='dataset'):
        if c == 1:
            f = open(path,'r')
            data = f.readlines()
            for i in data:
                self.image.append(i[:-1])
            print(self.image)
            f.close()
        else:
            self.images_path = '{}*.jpg'.format(path)
            for i in glob.glob(self.images_path):
                self.image.append(i)
    def generate_images(self):
        self.aug = iaa.Sequential([
            iaa.GaussianBlur(sigma=(0,3.0)), 
            iaa.LinearContrast((0.75,1.5)),
            # iaa.MultiplyAndAddToBrightness(add=(-50, 50))
        ])
        for i in self.image:
            print(i)
            img = cv2.imread(i)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            aug_img = self.aug(images=gray)
            cv2.imwrite(i,aug_img)
    def view_images(self,path='*.jpg'):
        if path == '*.jpg':
           pass
        else:
            img = cv2.imread(path)
            cv2.imshow('test',img)
            cv2.waitKey(0)
if __name__ == "__main__":
    # run aug
    ap = argparse.ArgumentParser()
    ap.add_argument('-p','--path',dest='path')
    ap.add_argument('-t','--text',dest='text')
    ap.add_argument('-c','--choose',dest='choose')
    ap.add_argument('-d','--dir',dest='dir')
    args = vars(ap.parse_args())
    d = DataAug()
    p = ImagePath('path.txt') 
    p.export()
    if args['dir'] != None:
        os.mkdir(args['dir'])
    if args['path'] != None:
        d.load_images(args['path'],args['choose'])
    if args['text'] != None:
        d.load_images(args['text'],args['choose'])
    else:
        d.load_images()
    d.generate_images()
    #d.view_images('lena1.jpg')
