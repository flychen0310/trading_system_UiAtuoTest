#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/20 21:25
# @Author: jackchen
import ddddocr


class OcrIdentify:

    def __init__(self):
        self.ocr = ddddocr.DdddOcr()

    def identify(self, pic_path):
        with open(pic_path, "rb") as f:
            image = f.read()
        return self.ocr.classification(image)
