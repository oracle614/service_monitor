from common.db_config import CONFIG
from common.utils import DB
from common.utils import DateFormat
monitor_db = DB(CONFIG.ALIYUN_MOCK)
date_format = DateFormat()

class DBLog:
    def failed_log(self, tc_name, result_id, failed_content):
        sql_failed_log = 'INSERT INTO service_product_failed_log (tc_name, result_id, failed_content) VALUES("{}", {}, "{}")'.format(tc_name, result_id, failed_content)
        monitor_db.update(sql_failed_log)
        sql_get_failed_log = 'select * from service_product_failed_log where tc_name = "{}" and result_id = {} and failed_content = "{}"'.format(tc_name, result_id, failed_content)
        get_fail_log = monitor_db.query(sql_get_failed_log)
        return get_fail_log[0]

if __name__ == '__main__':
    dblog = DBLog()
    print(dblog.failed_log('test_tc_name', 1, 'xxxxxxxx失败啦'))