#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/9 19:44
# @Author: jackchen
import pytest
from pytest_assume.plugin import assume


class TestAssert:

    # assume 断言失败是下面的用例还可以继续执行，assert不行
    def test_assert(self):
        with assume: assert "wiiliam" in "UI test"
        pytest.assume(1 + 1 == 3)
        assert 1 + 1 == 2
        print('success======>>>')
