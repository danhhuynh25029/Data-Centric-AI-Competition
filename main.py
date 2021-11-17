import cv2
import glob
import argparse
import imgaug.augmenters as iaa
class DataAug:
    def __init__(self):
        self.images_path = None
        self.image = []
        self.aug = None
    def load_images(self,path='*.jpg'):
        self.images_path = path
        for i in glob.glob(self.images_path):
            print(i)
    def generate_images(self):
        self.aug = iaa.Sequential([
            iaa.GaussianBlur(sigma=(0,3.0)), 
            iaa.LinearContrast((0.75,1.5))
        ])
        for i in self.image:
            aug_img = aug(images=i)
            cv2.imwrite(aug_img)
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
    args = vars(ap.parse_args())
    d = DataAug()
    if args['path'] != None:
        d.load_images(args['path'])
    else:
        d.load_images('lena1.jpg')
    d.generate_images()
    d.view_images('lena1.jpg')
