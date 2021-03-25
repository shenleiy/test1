# -*- coding:utf-8 -*-
import pymysql
import sys


class Mc(object):
    #  这里 注释连接的方法，是为了 实例化对象时，就创建连接。不许要单独处理连接了。
    #
    # def connDataBase(self):
    #     ''' 数据库连接 '''
    #
    #     self.db = pymysql.connect(self.host,self.username,self.password,self.port,self.database)
    #
    #     # self.cursor = self.db.cursor()
    #
    #     return self.db
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", passwd="****", db="***", port=3305,
                                  charset='utf8')

    # print(dbname)

    ''' 插入数据库操作 '''

    def insertDB(self, sql):
        self.cursor = self.db.cursor()
        try:
            # 执行sql
            self.cursor.execute(sql)
            # tt = self.cursor.execute(sql)  # 返回 插入数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    ''' 操作数据库数据删除 '''

    def deleteDB(self, sql):
        self.cursor = self.db.cursor()
        try:
            # 执行sql
            self.cursor.execute(sql)
            # tt = self.cursor.execute(sql) # 返回 删除数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    ''' 更新数据库操作 '''

    def updateDb(self, sql):
        self.cursor = self.db.cursor()
        try:
            # 执行sql
            self.cursor.execute(sql)
            # tt = self.cursor.execute(sql) # 返回 更新数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    '''数据库查询'''

    def selectDb(self, sql):
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)  # 返回 查询数据 条数 可以根据 返回值 判定处理结果
            data = self.cursor.fetchall()  # 返回所有记录列表
            print(data)
            print(type(data))
            print(data[1][1])
        except:
            print('Error: unable to fecth data')
        finally:
            self.cursor.close()
        # return data

    ''' 数据库连接关闭 '''

    def closeDb(self):
        self.db.close()


if __name__ == '__main__':
    mc = Mc()
    sql = 'SELECT * from xiaolu;'
    result = mc.selectDb(sql)
