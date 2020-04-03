import random
import ctypes
import time
import os

path2 = "./unsplashImageSpider/"
path = 'E:\\works-spring\\py-weibo\\i\\unsplashImageSpider\\'
while True:
    file = os.listdir(path)
    for i in file:
        print(i)
    filepath = path + random.choice(file)
    print(filepath)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)
    time.sleep(5)