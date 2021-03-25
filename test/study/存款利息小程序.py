while True:
    m = int(input('请输入你每月存款的金额:'))
    if m < 0:
        print('输入的数字错误，必须要大于0')
    else:
        print('本次每月存款设置的金额为{}元'.format(m))
        break

while True:
    n = int(input('请输入存款月数：'))
    if n < 0:
        print('输入的数字错误，必须要大于0')
    else:
        if 0 < n < 36:
            money = m * ((n + 1) / 2 * n) * ((2.6 / 100) / 12)
        elif 36 <= n < 60:
            money = m * ((n + 1) / 2 * n) * ((3.8 / 100) / 12)
        else:
            money = m * ((n + 1) / 2 * n) * ((4.2 / 100) / 12)
        print('你每月存{}元，预计存{}个月，到期可以获得的存款利息为{}元'.format(m, n, money))
        break
