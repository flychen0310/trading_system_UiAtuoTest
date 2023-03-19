#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/25 20:22
# @Author: jackchen
import yaml
from common.tools import get_project_path, sep


class GetConfig:
    def __init__(self):
        """
        获取yaml文件内容
        :return:
        """
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), 'r',
                  encoding='utf-8') as f:
            self.yaml_file = yaml.load(f, Loader=yaml.FullLoader)

    def get_username_pwd(self, user):
        # return self.yaml_file['username'], self.yaml_file['password']
        return self.yaml_file["user"][user]['username'],self.yaml_file["user"][user]['password']


    def get_url(self):
        return self.yaml_file["url"]


if __name__ == '__main__':
    # print(GetConfig().get_url())
    print(GetConfig().get_username_pwd('william'))