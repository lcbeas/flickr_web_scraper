import csv
import requests
import os
import sys
import time


def main():
    #print(sys.argv)
    #print(len(sys.argv))
    tags_dirty = sys.argv[1]
    MAX_COUNT = int(sys.argv[2])
    tags = tags_dirty.strip('[]').split(',')
   # print(tags)
    for i in tags:
        #print(i)
        a = 'python flickrGetUrl.py ' + '"' + i + '" ' + str(MAX_COUNT)
        b = 'python get_images.py ' + '"' + i +'"'+ '_urls.csv'
        #print(b)
        #print('python flickrGetUrl.py ', '"', i,  '" ',MAX_COUNT, sep = '')
        #print(f"python get_images.py '{i}'_urls.csv", sep = '')
        time.sleep(5)
        os.system(a)
        time.sleep(3)
        os.system(b)
    
if __name__ == '__main__':
    main()


