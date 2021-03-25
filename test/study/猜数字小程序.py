while True:
    num = int(input('请随机输入一个0~99之间的整数:'))
    if num > 99:
        print('输入的数字过大，不符合条件,请重新输入')
    elif num < 0:
        print('输入的数字过小，不符合条件,请重新输入')
    else:
        print('本次游戏设置的数字是{}'.format(num))
        break
print('---猜数字游戏开始---')
n = 1
while True:
    guess_num = int(input('第%d次输入数字:' % (n)))
    n += 1
    if guess_num > num:
        print('不好意思，你猜大了')
    elif guess_num < num:
        print('不好意思，你猜小了')
    else:
        print('恭喜你猜对了')
        break
    if n == 4:
        print('你的机会已经用完了')
        break
