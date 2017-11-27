from aynu.utils.Mydb import Mydb

mydb = Mydb()


def getproxy():
    sql = 'select * from ip_proxy ORDER BY rand() limit 1'
    res = mydb.query(sql)
    proxy_info = res[0]
    return proxy_info