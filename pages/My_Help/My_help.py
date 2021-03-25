from common import Element
import time
import random, re, string


class My_help(Element.Element):
    def __init__(self, driver):
        self.driver = driver
        X = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+}{"?:><|1234567890QWERTYUI偶怕是电饭锅和' \
            '健康路站下车vbnm1威海市立法是开发打发士大夫按时发到付刷卡好看撒哈撒饭喝口水都发的是发货快点发哈速度快'
        x = random.randint(1, 200)
        My_help.get_name(self, "帮助与反馈")
        print("点击帮助与反馈")

        My_help.get_name(self, "账号问题")
        print("\033[4;34m点击账号问题")
        zhanghao = ['1.账号注册', '2.账号登录', '3.忘记密码', '4.第三方账号登录', '5.修改个人信息', '6.修改账号密码']
        a = random.choice(zhanghao)
        print('随机点击', a)
        My_help.get_name(self, a)
        if a == '1.账号注册':
            My_help.find_name(self, '账号注册')
        elif a == '2.账号登录':
            My_help.find_name(self, '账号登录')
        elif a == '3.忘记密码':
            My_help.find_name(self, '忘记密码')
        elif a == '4.第三方账号登录':
            My_help.find_name(self, '第三方账号登录')
        elif a == '5.修改个人信息':
            My_help.find_name(self, '修改个人信息')
        else:
            My_help.find_name(self, '修改账号密码')
        My_help.get_name(self, "还没解决问题？")
        print('点击还没解决问题？，进入意见反馈页面')
        My_help.get_name(self, '账号问题')
        qusetion = ['账号问题', '设备添加', '设备管理', '功能异常', '场景模式', '其他问题']
        b = random.choice(qusetion)
        print('切换问题类型为：', b)
        time.sleep(1)
        My_help.get_name(self, b)
        My_help.find_name(self, b)
        nickname = random.sample(string.ascii_letters + string.digits + X, 200)
        My_help.get_Id(self, 'com.broadlink.auxair:id/et_feedback').send_keys(nickname)
        My_help.get_name(self, '提交')
        My_help.find_name(self, '账号问题')
        My_help.get_id(self, 'com.broadlink.auxair:id/iv_back')
        My_help.get_name(self, '账号问题')
        time.sleep(2)
        My_help.get_id(self, 'com.broadlink.auxair:id/rl_msg')
        My_help.find_name(self, b)
        My_help.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
        My_help.find_name(self, '帮助与反馈')

        My_help.get_name(self, "设备添加")
        print('\033[4;34m点击设备添加')
        tianjia = ['1、添加空调设备', '2、添加空调设备失败', '3、空调设备复位不成功']
        c = random.choice(tianjia)
        print('随机点击', c)
        My_help.get_name(self, c)
        if c == '1、添加空调设备':
            My_help.find_name(self, '添加空调设备')
        elif c == '2、添加空调设备失败':
            My_help.find_name(self, '添加空调设备失败')
        else:
            My_help.find_name(self, '空调设备复位不成功')
        My_help.get_name(self, "还没解决问题？")
        print('点击还没解决问题？，进入意见反馈页面')
        My_help.get_name(self, '设备添加')
        qusetion = ['账号问题', '设备添加', '设备管理', '功能异常', '场景模式', '其他问题']
        d = random.choice(qusetion)
        print('切换问题类型为：', d)
        time.sleep(1)
        My_help.get_name(self, d)
        My_help.find_name(self, d)
        My_help.get_Id(self, 'com.broadlink.auxair:id/et_feedback').send_keys(nickname)
        My_help.get_name(self, '提交')
        My_help.find_name(self, '设备添加')
        My_help.get_id(self, 'com.broadlink.auxair:id/iv_back')
        My_help.get_name(self, '设备添加')
        My_help.get_id(self, 'com.broadlink.auxair:id/rl_msg')
        My_help.find_name(self, d)
        My_help.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
        My_help.find_name(self, '帮助与反馈')

        My_help.get_name(self, "设备管理")
        print('\033[4;34m点击设备管理')
        guanli = ['1、修改空调设备名称', '2、空调设备删除', '3、如何设置睡眠DIY', '4、如何分享设备']
        e = random.choice(guanli)
        print('随机点击', e)
        My_help.get_name(self, e)
        if e == '1、修改空调设备名称':
            My_help.find_name(self, '修改空调设备名称')
        elif e == '2、空调设备删除':
            My_help.find_name(self, '空调设备删除')
        elif e == '3、如何设置睡眠DIY':
            My_help.find_name(self, '如何设置睡眠DIY')
        else:
            My_help.find_name(self, '如何分享设备')
        My_help.get_name(self, "还没解决问题？")
        print('点击还没解决问题？，进入意见反馈页面')
        My_help.get_name(self, '设备管理')
        qusetion = ['账号问题', '设备添加', '设备管理', '功能异常', '场景模式', '其他问题']
        f = random.choice(qusetion)
        print('切换问题类型为：', f)
        time.sleep(1)
        My_help.get_name(self, f)
        My_help.find_name(self, f)
        My_help.get_Id(self, 'com.broadlink.auxair:id/et_feedback').send_keys(nickname)
        My_help.get_name(self, '提交')
        My_help.find_name(self, '设备管理')
        My_help.get_id(self, 'com.broadlink.auxair:id/iv_back')
        My_help.get_name(self, '设备管理')
        My_help.get_id(self, 'com.broadlink.auxair:id/rl_msg')
        My_help.find_name(self, f)
        My_help.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
        My_help.find_name(self, '帮助与反馈')

        My_help.get_name(self, "功能异常")
        print('\033[4;34m点击功能异常')
        yichang = ['1、空调设备电量功能异常', '2、设置定时不执行', '3、显示的控制功能与空调型号不对应',
                   '4、设备列表页已经配网的空调设备消失', '5、设备控制页显示发生故障']
        g = random.choice(yichang)
        print('随机点击', g)
        My_help.get_name(self, g)
        if g == '1、空调设备电量功能异常':
            My_help.find_name(self, '空调设备电量功能异常')
        elif g == '2、设置定时不执行':
            My_help.find_name(self, '设置定时不执行')
        elif g == '3、显示的控制功能与空调型号不对应':
            My_help.find_name(self, '显示的控制功能与空调型号不对应')
        elif g == '4、设备列表页已经配网的空调设备消失':
            My_help.find_name(self, '设备列表页已经配网的空调设备消失')
        else:
            My_help.find_name(self, '设备控制页显示发生故障')
        My_help.get_name(self, "还没解决问题？")
        print('点击还没解决问题？，进入意见反馈页面')
        My_help.get_name(self, '功能异常')
        qusetion = ['账号问题', '设备添加', '设备管理', '功能异常', '场景模式', '其他问题']
        h = random.choice(qusetion)
        print('切换问题类型为：', h)
        time.sleep(1)
        My_help.get_name(self, h)
        My_help.find_name(self, h)
        My_help.get_Id(self, 'com.broadlink.auxair:id/et_feedback').send_keys(nickname)
        My_help.get_name(self, '提交')
        My_help.find_name(self, '功能异常')
        My_help.get_id(self, 'com.broadlink.auxair:id/iv_back')
        My_help.get_name(self, '功能异常')
        My_help.get_id(self, 'com.broadlink.auxair:id/rl_msg')
        My_help.find_name(self, h)
        My_help.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
        My_help.find_name(self, '帮助与反馈')

        My_help.get_name(self, "场景模式")
        print('\033[4;34m点击场景模式')
        changjing = ['1.如何添加场景模式', '2.场景功能设置未执行']
        m = random.choice(changjing)
        print('随机点击', m)
        My_help.get_name(self, m)
        if m == '1.如何添加场景模式':
            My_help.find_name(self, '如何添加场景模式')
        else:
            My_help.find_name(self, '场景功能设置未执行')
        My_help.get_name(self, "还没解决问题？")
        print('点击还没解决问题？，进入意见反馈页面')
        My_help.get_name(self, '场景模式')
        qusetion = ['账号问题', '设备添加', '设备管理', '功能异常', '场景模式', '其他问题']
        n = random.choice(qusetion)
        print('切换问题类型为：', n)
        time.sleep(1)
        My_help.get_name(self, n)
        My_help.find_name(self, n)
        My_help.get_Id(self, 'com.broadlink.auxair:id/et_feedback').send_keys(nickname)
        My_help.get_name(self, '提交')
        My_help.find_name(self, '场景模式')
        My_help.get_id(self, 'com.broadlink.auxair:id/iv_back')
        My_help.get_name(self, '场景模式')
        My_help.get_id(self, 'com.broadlink.auxair:id/rl_msg')
        My_help.find_name(self, n)
        My_help.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
        My_help.find_name(self, '帮助与反馈')

        My_help.get_name(self, "其他问题")
        print('\033[4;34m点击其他问题')
        wenti = ['1、空调报装、报修', '2、空调设备离线']
        o= random.choice(wenti)
        print('随机点击', o)
        My_help.get_name(self, o)
        if o == '1、空调报装、报修':
            My_help.find_name(self, '空调报装、报修')
        else:
            My_help.find_name(self, '空调设备离线')
        My_help.get_name(self, "还没解决问题？")
        print('点击还没解决问题？，进入意见反馈页面')
        My_help.get_name(self, '其他问题')
        qusetion = ['账号问题', '设备添加', '设备管理', '功能异常', '场景模式', '其他问题']
        p = random.choice(qusetion)
        print('切换问题类型为：', p)
        time.sleep(1)
        My_help.get_name(self, p)
        My_help.find_name(self, p)
        My_help.get_Id(self, 'com.broadlink.auxair:id/et_feedback').send_keys(nickname)
        My_help.get_name(self, '提交')
        My_help.find_name(self, '其他问题')
        My_help.get_id(self, 'com.broadlink.auxair:id/iv_back')
        My_help.get_name(self, '其他问题')
        My_help.get_id(self, 'com.broadlink.auxair:id/rl_msg')
        My_help.find_name(self, p)
        My_help.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
        My_help.find_name(self, '帮助与反馈')
