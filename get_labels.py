import glob
class ImagePath:
    def __init__(self,path):
        self.path = path
        self.list_path = []
    def showPath(self):
        print(self.path)
        label_path = glob.glob(self.path)
        for i in label_path:
            # print(i)
            f = open(i,'r')
            text = f.readlines()
            #print(text)
            tmp = False
            for t in text:
                if t[0] == '0' or t[0] == '2':
                    tmp = True
                    break
            if tmp == True:
                if i not in self.list_path:
                    s = '{}\n'.format(i)
                    self.list_path.append(s)
            f.close()
    def export(self):
        f = open('path.txt','w')
        for i in self.list_path:
            f.write(i)
        f.close()
        print(self.list_path)

if __name__ == "__main__":
    p = ImagePath('dataset/labels/train/*.txt')
    p.showPath()
    p.export()
