#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2023/8/4 10:23
# file: uploadORpush_files_to_cos.py
# author: qinxi
# email: 1023495336@qq.com

import subprocess
import os

def install_cos_cli():
    try:
        # 自动下载COS CLI工具并设置权限
        subprocess.check_call(['wget', 'https://cosbrowser.cloud.tencent.com/software/coscli/coscli-linux'])
        subprocess.check_call(['mv', 'coscli-linux', '/usr/bin/coscli'])
        subprocess.check_call(['chmod', '755', '/usr/bin/coscli'])
        print("COS CLI 工具下载并设置权限成功！")

        # 自动配置COS CLI工具
        config_content = """
        cos:
          base:
            secretid: 腾讯云secretid
            secretkey: 腾讯云secretkey
            sessiontoken: 
            protocol: https
          buckets:
          - name: buckets名字
            alias: 
            region: ""
            endpoint: cos.ap-shanghai.myqcloud.com
            ofs: false
        """
        with open(os.path.expanduser("~/.cos.yaml"), "w") as config_file:
            config_file.write(config_content)

        print("COS CLI 工具配置成功！")

        # 打印案例
        print("例：下载单个文件：")
        print(" coscli cp cos://bucket1/example.txt ~/example.txt")
        print("例：将cos桶中的example文件夹下的所有文件下载到本地test文件夹下：")
        print(" coscli cp cos://bucket1/example/ ~/test/ -r")
        print("\n")
        print("例：上传单个文件：")
        print(" coscli cp ~/example.txt cos://bucket1/example.txt")
        print("例：将本地文件夹下的所有文件上传至cos桶中的example 文件夹下：")
        print(" coscli cp ./model-sft/ cos://data-backup-1318812101/glm-a800-02_model-sft/ -r")
    except subprocess.CalledProcessError as e:
        print("安装或配置失败：", e)

if __name__ == "__main__":
    install_cos_cli()
