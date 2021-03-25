from tkinter import *

root = Tk()
y = Scrollbar(root)


class MY_GUI():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        self.PlatformName = Label(self.init_window_name, text="platformName:")
        self.PlatformVersion = Label(self.init_window_name, text="platformVersion:")
        self.DeviceName = Label(self.init_window_name, text="deviceName:")
        self.AppPackage = Label(self.init_window_name, text="appPackage:")
        self.AppActivity = Label(self.init_window_name, text="appActivity:")
        self.NoReset = Label(self.init_window_name, text="noReset:")
        self.button_ok = Button(self.init_window_name, text="ok", width=10, command=self.text)
        self.button_quit = Button(self.init_window_name, text="退出", width=10, command=self.quit)
        self.button_true = Listbox(root, width=10, height=1, yscrollcommand=y.set)
        for item in ['true', 'false']:
            self.button_true.insert('end', item)
        y.config(command=self.button_true.yview)

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("手机参数设置工具_v1.2")  # 窗口名
        # self.init_window_name.geometry('568x301+10+10')  # 窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        # self.init_window_name["bg"] = "black"  # 窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        self.init_window_name.attributes("-alpha", 1)  # 虚化，值越小虚化程度越高
        self.PlatformName.grid(row=0, column=0)
        self.PlatformVersion.grid(row=1, column=0)
        self.DeviceName.grid(row=2, column=0)
        self.AppPackage.grid(row=3, column=0)
        self.AppActivity.grid(row=4, column=0)
        self.NoReset.grid(row=5, column=0)
        self.button_true.grid(row=5, column=1)
        self.button_ok.grid(row=6, column=0)
        self.button_quit.grid(row=6, column=1)
        self.platformName = Text(self.init_window_name, width=30, height=1, )  # 原始数据录入框
        self.platformName.grid(row=0, column=1)
        self.platformVersion = Text(self.init_window_name, width=30, height=1)  # 原始数据录入框
        self.platformVersion.grid(row=1, column=1)
        self.deviceName = Text(self.init_window_name, width=30, height=1)  # 原始数据录入框
        self.deviceName.grid(row=2, column=1)
        self.appPackage = Text(self.init_window_name, width=30, height=1)  # 原始数据录入框
        self.appPackage.grid(row=3, column=1)
        self.init_data_Text = Text(self.init_window_name, width=30, height=1)  # 原始数据录入框
        self.init_data_Text.grid(row=4, column=1)

    def text(self):
        platformName = self.platformName.get('1.0', END)
        print(platformName)
        platformVersion = self.platformVersion.get('1.0', END)
        print(platformVersion)
        deviceName = self.deviceName.get('1.0', END)
        print(deviceName)
        appPackage = self.appPackage.get('1.0', END)
        print(appPackage)

    def update(self):
        root.update()
        self.init_window_name["bg"] = "black"
        pass

    def quit(self):
        root.quit()
        pass


def start():
    ZMJ_PORTAL = MY_GUI(root)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    root.mainloop()


start()
