from common.db_config import CONFIG
from common.utils import DB
from common.utils import DateFormat
monitor_db = DB(CONFIG.ALIYUN_MOCK)
date_format = DateFormat()

class DBLog:
    def failed_log(self, product_id, tc_name, result_id, failed_content):
        sql_failed_log = 'INSERT INTO service_product_failed_log (product_id, tc_name, result_id, failed_content) VALUES({}, "{}", {}, "{}")'.format(product_id, tc_name, result_id, failed_content)
        monitor_db.update(sql_failed_log)
        sql_get_failed_log = 'select * from service_product_failed_log where tc_name = "{}" and result_id = {} and failed_content = "{}"'.format(tc_name, result_id, failed_content)
        get_fail_log = monitor_db.query(sql_get_failed_log)
        return get_fail_log[0]

    def get_failed_count(self,product_id=None, start_time=None, end_time=None):
        sql_get_failed_log = 'select count(1) from service_product_failed_log where product_id={} and sys_time >= "{}" and sys_time <="{}"'.format(product_id, start_time, end_time)
        print(sql_get_failed_log)
        return monitor_db.query(sql_get_failed_log)[0]['count(1)']


if __name__ == '__main__':
    dblog = DBLog()
    print(dblog.failed_log(1, 'test_tc_name', 2, 'xxxxxxxx失败啦'))
    print(dblog.get_failed_count(1, '2018-8-13 00:0000', '2018-8-15 00:00:00'))