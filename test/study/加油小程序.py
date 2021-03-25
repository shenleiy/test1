while True:
    gasoline = input('请输入车子的剩余油量:')
    a = 50 - int(gasoline)
    print('需要加油量：', a)
    if a > 20:
        b = 20 * 6 + (a - 20) * 5.5  # 加油站1
        c = 20 * 5.5 + (a - 20) * 6  # 加油站2
        if b > c:
            print('加油站2便宜,需要金额{}元'.format(c))
        elif b < c:
            print('加油站1便宜,需要金额{}元'.format(b))
        else:
            print('两家加油站价格相同，需要金额{}元'.format(b))
    elif 0 < a <= 20:
        b = a * 6  # 加油站1
        c = a * 5.5  # 加油站2
        print('加油站2便宜,需要金额{}元'.format(c))
    else:
        print('不需要加油')

