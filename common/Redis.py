import redis

ip = 'r-bp1clh757sovwmrd23pd.redis.rds.aliyuncs.com'
password = 'SHEhe123'


class Code:
    @staticmethod
    def search_code(phone):
        # 方法一
        # r = redis.Redis(host=ip, password=password, port=6379, db='0', decode_responses=True)
        # res = r.get('domain_token:031fd83a03d5403a963fb45d33d85a76:00e7fe2cbfcd4c4296ed295f189c3a5c')
        # print(res)
        # 方法二
        pool = redis.ConnectionPool(host=ip, password=password, port=6379, db='0', decode_responses=True)
        r = redis.StrictRedis(connection_pool=pool)
        res = r.get('domain_phone_code:031fd83a03d5403a963fb45d33d85a76:%d:~' % phone)
        return res


# search_code(15888504457)
# re = Code().search_code(15888504457)
# print(re)
# Code().search_code(15888504457)
if __name__ == '__main__':
    a = Code.search_code(15888504457)
    print(a)
