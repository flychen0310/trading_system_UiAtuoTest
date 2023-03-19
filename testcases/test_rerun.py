#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/9 19:38
# @Author: jackchen
import pytest
import random


class TestRerun:
    # 最多重新跑5次，每次间隔时间为1
    @pytest.mark.flaky(reruns=5, reruns_delay=1)
    def test_rerun(self):
        num = random.randint(1, 3)
        print(num)
        if num != 1:
            print("失败")
            raise Exception("fails")
        else:
            print("成功")
