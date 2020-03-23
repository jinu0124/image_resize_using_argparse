import argparse
from PIL import Image # opencv, skimage 등 다양한 패키지 사용가능
import os
# 폴더내의 모든 이미지들을 system명령어 인자를 이용하여 새 폴더 생성하여 모든 이미지 Resizing하는 프로그램

class execute:
    def __init__(self, dictionary):
        super().__init__()
        self.rescale_size_x = dictionary['size'][0]
        self.rescale_size_y = dictionary['size'][1]
        self.folder_name = dictionary['name'][0]
        self.dir = dictionary['dir'][0]
        self.resize_compute()

    def resize_compute(self):
        if self.folder_name not in os.listdir(self.dir):
            os.mkdir(self.dir + '/' + self.folder_name + '/') # 폴더 생성
        save_dir = os.path.join(self.dir, self.folder_name)
        for img in os.listdir(self.dir): # 폴더 내의 모든 이미지에 대해 수행 계획, for 빼고 단일 이미지에 대해서 수행도 가능하다.
            ext = os.path.splitext(img)
            if 'jpg' not in str(ext[1]):
                continue
            im = Image.open(os.path.join(self.dir, img)) # open image from directory
            im_resized = im.resize([self.rescale_size_x, self.rescale_size_y], Image.ANTIALIAS) #image resize to size
            basename = os.path.basename(img)
            im_resized.save(save_dir + '/Resized_' + basename) # image save
        files = os.listdir(save_dir)
        count = len(files)
        print(str(count) + 'files complete')

if __name__ == '__main__':
    dictionary = dict()
    resize = []

    parser = argparse.ArgumentParser(description='rescale image')

    parser.add_argument('-r', '--resize', type=int, required=True, nargs=2)
    parser.add_argument('-n', '--name', type=str, required=True, nargs=1)
    parser.add_argument('-d', '--directory', type=str, required=True, nargs=1)

    args = parser.parse_args()

    for i in args.resize:
        resize.append(i)
    name = args.name # list type output
    dir = args.directory
    dictionary['size'] = resize
    dictionary['name'] = name
    dictionary['dir'] = dir

    execute(dictionary) # Dict type send


