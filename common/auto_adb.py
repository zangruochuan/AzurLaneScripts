# -*- coding: utf-8 -*-
import os
import subprocess
import platform


class auto_adb:
    def __init__(self):
        try:
            adb_path = 'adb\\platform-tools\\adb.exe'
            subprocess.Popen([adb_path], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            self.adb_path = adb_path
        except OSError:
            if platform.system() == 'Windows':
                adb_path = os.path.join('adb', "platform-tools", 'adb.exe')
                try:
                    subprocess.Popen(
                        [adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    self.adb_path = adb_path
                except OSError:
                    pass
            else:
                try:
                    subprocess.Popen(
                        [adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except OSError:
                    pass
            print('请安装 ADB 及驱动并配置环境变量')
            print('具体链接: https://github.com/wangshub/wechat_jump_game/wiki')
            exit(1)

    def get_screen(self):
        process = os.popen(self.adb_path + ' shell wm size')
        output = process.read()
        return output

    def get_size(self):
        output = self.get_screen()
        output = output.split(':')[1][1:]
        output = output.split('x')
        return int(output[0]), int(output[1])

    def run(self, raw_command):
        command = '{} {}'.format(self.adb_path, raw_command)
        process = os.popen(command)
        output = process.read()
        return output

    def test_device(self):
        print('检查设备是否连接...')
        command_list = [self.adb_path, 'devices']
        process = subprocess.Popen(
            command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.communicate()
        if output[0].decode('utf8') == 'List of devices attached\n\n':
            print('未找到设备')
            print('adb 输出:')
            for each in output:
                print(each.decode('utf8'))
            exit(1)
        print('设备已连接')
        print('adb 输出:')
        for each in output:
            print(each.decode('utf8'))

    def test_density(self):
        process = os.popen(self.adb_path + ' shell wm density')
        output = process.read()
        return output

    def test_device_detail(self):
        process = os.popen(self.adb_path + ' shell getprop ro.product.device')
        output = process.read()
        return output

    def test_device_os(self):
        process = os.popen(
            self.adb_path + ' shell getprop ro.build.version.release')
        output = process.read()
        return output

    def adb_path(self):
        return self.adb_path

    def tap_scale(self, pos, scale):
        scaled_pos = int(pos[0] * scale[0]), int(pos[1] * scale[1])
        print(scaled_pos)
        self.run('shell input tap {} {}'.format(scaled_pos[0], scaled_pos[1]))
        return scaled_pos

    def swipe_scale(self, pos, scale):
        scaled_mid = int(960/2*scale[0]), int(443/2*scale[1])
        scaled_pos = int(pos[0]*scale[0]), int(pos[1]*scale[1])
        print(scaled_pos)
        print(
            f'shell input swipe {scaled_mid[0]} {scaled_mid[1]} {scaled_mid[0]+scaled_pos[0]} {scaled_mid[1]+scaled_pos[1]} {1000}')
        self.run(
            f'shell input swipe {scaled_mid[0]} {scaled_mid[1]} {scaled_mid[0]+scaled_pos[0]} {scaled_mid[1]+scaled_pos[1]} {1000}')

