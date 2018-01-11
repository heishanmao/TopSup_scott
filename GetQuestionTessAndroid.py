# -*- coding: utf-8 -*-

# @Author  : Scott
# @Time    : 2018/1/8 20:38
# @desc    : 答题闯关辅助，截屏 ，OCR 识别，百度搜索


from PIL import Image
from common import screenshot, ocr, methods
import time
import threading

if __name__ == '__main__':
        # 计时器
        start = time.clock()

        # 截图
        screenshot.check_screenshot()
        img = Image.open("./screenshot.png")

        # 文字识别
        question, choices = ocr.ocr_img(img)

        # 启用多线程
        threads = []
        t1 = threading.Thread(target=methods.run_algorithm, args=(1, question, choices,))
        threads.append(t1)
        t2 = threading.Thread(target=methods.run_algorithm, args=(2, question, choices,))
        threads.append(t2)
        t3 = threading.Thread(target=methods.run_algorithm, args=(0, question, choices,))
        threads.append(t3)
        for t in threads:
            t.setDaemon(False)
            t.start()

        # 结束
        end = time.clock()
        print("耗时: {0:>5.3}s".format(end - start))

